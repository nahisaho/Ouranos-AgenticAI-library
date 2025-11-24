# Frameworks for Frontend Specialist

This file provides detailed definitions and application guidance for the frameworks used in this prompt.

---

### React Best Practices

**Component Design Patterns**:
```typescript
// Compound components
const Card = ({ children }) => <div className="card">{children}</div>;
Card.Header = ({ children }) => <header className="card-header">{children}</header>;
Card.Body = ({ children }) => <main className="card-body">{children}</main>;
Card.Footer = ({ children }) => <footer className="card-footer">{children}</footer>;

// Render props pattern
const DataFetcher = ({ url, children }) => {
  const [data, loading, error] = useFetch(url);
  return children({ data, loading, error });
};

// Higher-order component
const withAuth = (WrappedComponent) => {
  return (props) => {
    const { user } = useAuth();
    if (!user) return <Login />;
    return <WrappedComponent {...props} />;
  };
};
```

### Vue Composition API Patterns

```typescript
// Composable logic
export function useApi<T>(url: string) {
  const data = ref<T | null>(null);
  const loading = ref(true);
  const error = ref<string | null>(null);

  const fetchData = async () => {
    try {
      loading.value = true;
      const response = await fetch(url);
      data.value = await response.json();
    } catch (err) {
      error.value = err.message;
    } finally {
      loading.value = false;
    }
  };

  onMounted(fetchData);
  
  return { data, loading, error, refetch: fetchData };
}
```

### Performance Optimization Techniques

**Bundle Optimization**:
- Dynamic imports for code splitting
- Tree shaking configuration
- Module federation for micro-frontends
- Asset optimization and compression

**Runtime Optimization**:
- Memoization strategies
- Virtual scrolling for large lists
- Image lazy loading
- Service worker implementation

### Modern Build Tooling

**Vite Configuration**:
```typescript
export default defineConfig({
  plugins: [
    react(),
    vitePWA({
      registerType: 'autoUpdate',
      workbox: {
        globPatterns: ['**/*.{js,css,html,ico,png,svg}']
      }
    })
  ],
  build: {
    rollupOptions: {
      output: {
        manualChunks(id) {
          if (id.includes('node_modules')) {
            return 'vendor';
          }
        }
      }
    }
  }
});
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
  - Main Prompt: `prompts/copilot/prompts/design-development/frontend-specialist.md`
  - Examples: `rag/design-development/frontend-specialist/examples.md`
  - Methodologies: `rag/design-development/frontend-specialist/methodologies.md`
