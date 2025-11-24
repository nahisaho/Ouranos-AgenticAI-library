# Frameworks for Database Architect

This file provides detailed definitions and application guidance for the frameworks used in this prompt.

---

### SQL Database Design and Optimization

```sql
-- Comprehensive PostgreSQL database design example
CREATE DATABASE ecommerce_platform;

-- Users table with proper constraints and indexes
CREATE TABLE users (
    user_id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    email VARCHAR(255) UNIQUE NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    date_of_birth DATE,
    phone VARCHAR(20),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    email_verified BOOLEAN DEFAULT FALSE,
    
    -- Constraints
    CONSTRAINT chk_email_format CHECK (email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'),
    CONSTRAINT chk_username_length CHECK (length(username) >= 3),
    CONSTRAINT chk_birth_date CHECK (date_of_birth < CURRENT_DATE)
);

-- Optimized indexes
CREATE INDEX idx_users_email ON users (email);
CREATE INDEX idx_users_username ON users (username);
CREATE INDEX idx_users_active_created ON users (is_active, created_at DESC);
CREATE INDEX idx_users_last_name_first_name ON users (last_name, first_name);

-- Products table with hierarchical categories
CREATE TABLE categories (
    category_id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name VARCHAR(100) NOT NULL,
    parent_category_id BIGINT REFERENCES categories(category_id),
    path LTREE, -- Hierarchical path using PostgreSQL ltree
    is_active BOOLEAN DEFAULT TRUE
);

CREATE INDEX idx_categories_path_gist ON categories USING GIST (path);
CREATE INDEX idx_categories_parent ON categories (parent_category_id);

CREATE TABLE products (
    product_id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    sku VARCHAR(50) UNIQUE NOT NULL,
    category_id BIGINT REFERENCES categories(category_id),
    price DECIMAL(10,2) NOT NULL CHECK (price >= 0),
    cost DECIMAL(10,2) CHECK (cost >= 0),
    inventory_quantity INTEGER DEFAULT 0 CHECK (inventory_quantity >= 0),
    weight_grams INTEGER,
    dimensions_json JSONB,
    tags TEXT[],
    search_vector TSVECTOR,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

-- Full-text search setup
CREATE INDEX idx_products_search_gin ON products USING GIN (search_vector);
CREATE INDEX idx_products_category_active ON products (category_id, is_active);
CREATE INDEX idx_products_price ON products (price) WHERE is_active = TRUE;

-- Trigger to maintain search vector
CREATE OR REPLACE FUNCTION update_product_search_vector()
RETURNS TRIGGER AS $$
BEGIN
    NEW.search_vector := to_tsvector('english', COALESCE(NEW.name, '') || ' ' || COALESCE(NEW.description, ''));
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trig_update_product_search
    BEFORE INSERT OR UPDATE ON products
    FOR EACH ROW EXECUTE FUNCTION update_product_search_vector();
```

### NoSQL Database Design

```javascript
// MongoDB collection design examples

// Users collection with embedded and referenced data
db.createCollection("users", {
   validator: {
      $jsonSchema: {
         bsonType: "object",
         required: ["email", "username", "passwordHash", "createdAt"],
         properties: {
            email: {
               bsonType: "string",
               pattern: "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
            },
            username: {
               bsonType: "string",
               minLength: 3,
               maxLength: 50
            },
            passwordHash: { bsonType: "string" },
            profile: {
               bsonType: "object",
               properties: {
                  firstName: { bsonType: "string" },
                  lastName: { bsonType: "string" },
                  dateOfBirth: { bsonType: "date" },
                  avatar: { bsonType: "string" }
               }
            },
            addresses: {
               bsonType: "array",
               items: {
                  bsonType: "object",
                  properties: {
                     type: { enum: ["billing", "shipping"] },
                     street: { bsonType: "string" },
                     city: { bsonType: "string" },
                     state: { bsonType: "string" },
                     zipCode: { bsonType: "string" },
                     country: { bsonType: "string" },
                     isDefault: { bsonType: "bool" }
                  }
               }
            },
            preferences: {
               bsonType: "object",
               properties: {
                  language: { bsonType: "string" },
                  currency: { bsonType: "string" },
                  notifications: {
                     bsonType: "object",
                     properties: {
                        email: { bsonType: "bool" },
                        sms: { bsonType: "bool" },
                        push: { bsonType: "bool" }
                     }
                  }
               }
            },
            isActive: { bsonType: "bool" },
            emailVerified: { bsonType: "bool" },
            createdAt: { bsonType: "date" },
            updatedAt: { bsonType: "date" }
         }
      }
   }
});

// Indexes for users collection
db.users.createIndex({ "email": 1 }, { unique: true });
db.users.createIndex({ "username": 1 }, { unique: true });
db.users.createIndex({ "isActive": 1, "createdAt": -1 });
db.users.createIndex({ "profile.lastName": 1, "profile.firstName": 1 });

// Products collection with denormalized data
db.createCollection("products", {
   validator: {
      $jsonSchema: {
         bsonType: "object",
         required: ["name", "sku", "price", "category"],
         properties: {
            name: { bsonType: "string", maxLength: 255 },
            description: { bsonType: "string" },
            sku: { bsonType: "string", maxLength: 50 },
            category: {
               bsonType: "object",
               required: ["id", "name"],
               properties: {
                  id: { bsonType: "objectId" },
                  name: { bsonType: "string" },
                  path: { bsonType: "string" }
               }
            },
            pricing: {
               bsonType: "object",
               required: ["price"],
               properties: {
                  price: { bsonType: "decimal", minimum: 0 },
                  cost: { bsonType: "decimal", minimum: 0 },
                  currency: { bsonType: "string" },
                  discounts: {
                     bsonType: "array",
                     items: {
                        bsonType: "object",
                        properties: {
                           type: { enum: ["percentage", "fixed"] },
                           value: { bsonType: "decimal" },
                           startDate: { bsonType: "date" },
                           endDate: { bsonType: "date" }
                        }
                     }
                  }
               }
            },
            inventory: {
               bsonType: "object",
               properties: {
                  quantity: { bsonType: "int", minimum: 0 },
                  reservedQuantity: { bsonType: "int", minimum: 0 },
                  reorderLevel: { bsonType: "int" },
                  maxStock: { bsonType: "int" }
               }
            },
            attributes: {
               bsonType: "object",
               properties: {
                  weight: { bsonType: "decimal" },
                  dimensions: {
                     bsonType: "object",
                     properties: {
                        length: { bsonType: "decimal" },
                        width: { bsonType: "decimal" },
                        height: { bsonType: "decimal" },
                        unit: { enum: ["cm", "in"] }
                     }
                  },
                  color: { bsonType: "string" },
                  size: { bsonType: "string" },
                  material: { bsonType: "string" }
               }
            },
            tags: {
               bsonType: "array",
               items: { bsonType: "string" }
            },
            images: {
               bsonType: "array",
               items: {
                  bsonType: "object",
                  properties: {
                     url: { bsonType: "string" },
                     alt: { bsonType: "string" },
                     isPrimary: { bsonType: "bool" },
                     order: { bsonType: "int" }
                  }
               }
            },
            seo: {
               bsonType: "object",
               properties: {
                  title: { bsonType: "string" },
                  description: { bsonType: "string" },
                  keywords: {
                     bsonType: "array",
                     items: { bsonType: "string" }
                  }
               }
            },
            isActive: { bsonType: "bool" },
            createdAt: { bsonType: "date" },
            updatedAt: { bsonType: "date" }
         }
      }
   }
});

// Indexes for products collection
db.products.createIndex({ "sku": 1 }, { unique: true });
db.products.createIndex({ "category.id": 1, "isActive": 1 });
db.products.createIndex({ "pricing.price": 1 });
db.products.createIndex({ "tags": 1 });
db.products.createIndex({ "name": "text", "description": "text", "tags": "text" });
db.products.createIndex({ "isActive": 1, "createdAt": -1 });
```

### Database Performance Optimization

```python
# Advanced query optimization and performance tuning
class QueryOptimizer:
    def __init__(self, db_connection):
        self.db = db_connection
        
    async def analyze_slow_queries(self) -> List[Dict[str, Any]]:
        """Identify and analyze slow queries"""
        
        query = """
        SELECT 
            query,
            calls,
            total_exec_time,
            mean_exec_time,
            stddev_exec_time,
            rows,
            100.0 * shared_blks_hit / NULLIF(shared_blks_hit + shared_blks_read, 0) AS hit_percent,
            100.0 * total_exec_time / SUM(total_exec_time) OVER() AS time_percent
        FROM pg_stat_statements 
        WHERE mean_exec_time > 100 -- Queries taking more than 100ms on average
        ORDER BY total_exec_time DESC
        LIMIT 20
        """
        
        return await self.db.fetch_all(query)
    
    async def suggest_index_optimizations(self, table_name: str) -> List[Dict[str, Any]]:
        """Suggest index optimizations for a table"""
        
        # Find unused indexes
        unused_indexes_query = """
        SELECT 
            indexrelname as index_name,
            idx_scan as index_scans,
            pg_size_pretty(pg_relation_size(indexrelname::regclass)) as index_size,
            pg_get_indexdef(indexrelid) as index_definition
        FROM pg_stat_user_indexes 
        WHERE schemaname = 'public'
        AND relname = %s
        AND idx_scan = 0
        ORDER BY pg_relation_size(indexrelname::regclass) DESC
        """
        
        # Find tables with low index usage
        low_usage_query = """
        SELECT 
            relname as table_name,
            seq_scan as sequential_scans,
            seq_tup_read as sequential_tuples_read,
            idx_scan as index_scans,
            idx_tup_fetch as index_tuples_fetched,
            ROUND(100.0 * idx_scan / NULLIF(seq_scan + idx_scan, 0), 2) as index_usage_percent
        FROM pg_stat_user_tables 
        WHERE relname = %s
        """
        
        unused_indexes = await self.db.fetch_all(unused_indexes_query, (table_name,))
        usage_stats = await self.db.fetch_one(low_usage_query, (table_name,))
        
        return {
            'unused_indexes': unused_indexes,
            'usage_statistics': usage_stats
        }
    
    async def optimize_table_statistics(self, table_name: str):
        """Update table statistics for better query planning"""
        
        # Analyze table to update statistics
        analyze_query = f"ANALYZE {table_name}"
        await self.db.execute(analyze_query)
        
        # Get table statistics
        stats_query = """
        SELECT 
            attname as column_name,
            n_distinct,
            most_common_vals,
            most_common_freqs,
            histogram_bounds
        FROM pg_stats 
        WHERE tablename = %s
        ORDER BY attname
        """
        
        return await self.db.fetch_all(stats_query, (table_name,))
```

---

---

## Framework Integration Strategies

### Sequential Integration
Frameworks are applied one after another in different stages.

**When to use**: When frameworks build on each other logically.

### Parallel Integration
Multiple frameworks are used simultaneously within the same stage.

**When to use**: When frameworks provide complementary perspectives.

### Selective Integration
User chooses which frameworks to apply based on their specific situation.

**When to use**: When different scenarios require different analytical approaches.

---

## Best Practices

1. **Start Simple**: Don't overwhelm with too many frameworks initially
2. **Explain Why**: Always clarify the purpose and value of each framework
3. **Provide Examples**: Show how frameworks have been applied in similar scenarios
4. **Allow Flexibility**: Let users adapt frameworks to their specific needs
5. **Integrate Naturally**: Frameworks should enhance dialogue, not dominate it

---

## Version Information

- **Version**: 1.0.0
- **Last Updated**: 2025-11-24
- **Related Files**: 
  - Main Prompt: `prompts/copilot/prompts/design-development/database-architect.md`
  - Examples: `rag/design-development/database-architect/examples.md`
  - Methodologies: `rag/design-development/database-architect/methodologies.md`
