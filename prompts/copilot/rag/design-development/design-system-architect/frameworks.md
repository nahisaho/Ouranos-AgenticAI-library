# Frameworks for Design System Architect

This file provides detailed definitions and application guidance for the frameworks used in this prompt.

---

### Atomic Design

**Created by**: Brad Frost

**Purpose**: Systematic approach to building design systems

**Five Levels**:
1. **Atoms**: HTML tags, labels, inputs, buttons
2. **Molecules**: Form fields, search boxes
3. **Organisms**: Headers, forms, product grids
4. **Templates**: Page layouts with placeholder content
5. **Pages**: Specific instances with real content

**Benefits**:
- Encourages reusability
- Creates consistent vocabulary
- Facilitates collaboration
- Scales well

### Design Tokens

**Purpose**: Platform-agnostic design decisions

**Token Types**:
- **Global tokens**: Base values (color-blue-500)
- **Alias tokens**: Semantic names (color-primary)
- **Component tokens**: Component-specific (button-background-color)

**Token Management**:
- Store in JSON, YAML, or JavaScript
- Transform with Style Dictionary
- Generate platform-specific code (CSS, iOS, Android)
- Version control

### WCAG 2.1 Guidelines

**Four Principles (POUR)**:
1. **Perceivable**: Information can be perceived
2. **Operable**: UI components are operable
3. **Understandable**: Information and operation are understandable
4. **Robust**: Content is robust enough for assistive technologies

**Conformance Levels**:
- **Level A**: Minimum (basic accessibility)
- **Level AA**: Mid-range (recommended target)
- **Level AAA**: Highest (not always achievable)

### Component API Design Patterns

**Composition Pattern**:
```tsx
<Card>
  <CardHeader>Title</CardHeader>
  <CardContent>Content here</CardContent>
  <CardFooter>Footer</CardFooter>
</Card>
```

**Render Props Pattern**:
```tsx
<Dropdown>
  {({ isOpen }) => (
    <div>Dropdown is {isOpen ? 'open' : 'closed'}</div>
  )}
</Dropdown>
```

**Compound Components**:
```tsx
<Tabs defaultValue="tab1">
  <TabsList>
    <TabsTrigger value="tab1">Tab 1</TabsTrigger>
    <TabsTrigger value="tab2">Tab 2</TabsTrigger>
  </TabsList>
  <TabsContent value="tab1">Content 1</TabsContent>
  <TabsContent value="tab2">Content 2</TabsContent>
</Tabs>
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
  - Main Prompt: `prompts/copilot/prompts/design-development/design-system-architect.md`
  - Examples: `rag/design-development/design-system-architect/examples.md`
  - Methodologies: `rag/design-development/design-system-architect/methodologies.md`
