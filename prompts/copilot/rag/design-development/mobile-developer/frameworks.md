# Frameworks for Mobile Developer

This file provides detailed definitions and application guidance for the frameworks used in this prompt.

---

### Native iOS Development (SwiftUI)

```swift
// Modern SwiftUI architecture with MVVM
struct ContentView: View {
    @StateObject private var viewModel = ContentViewModel()
    
    var body: some View {
        NavigationView {
            List(viewModel.items) { item in
                ItemRowView(item: item)
            }
            .navigationTitle("Items")
            .refreshable {
                await viewModel.refresh()
            }
        }
        .task {
            await viewModel.loadData()
        }
    }
}

@MainActor
class ContentViewModel: ObservableObject {
    @Published var items: [Item] = []
    @Published var isLoading = false
    
    private let service: ItemService
    
    init(service: ItemService = ItemService()) {
        self.service = service
    }
    
    func loadData() async {
        isLoading = true
        defer { isLoading = false }
        
        do {
            items = try await service.fetchItems()
        } catch {
            // Handle error
        }
    }
}
```

### Native Android Development (Jetpack Compose)

```kotlin
@Composable
fun ItemListScreen(
    viewModel: ItemListViewModel = hiltViewModel()
) {
    val uiState by viewModel.uiState.collectAsState()
    
    LazyColumn {
        items(uiState.items) { item ->
            ItemCard(
                item = item,
                onItemClick = { viewModel.selectItem(item.id) }
            )
        }
    }
    
    if (uiState.isLoading) {
        CircularProgressIndicator()
    }
}

@HiltViewModel
class ItemListViewModel @Inject constructor(
    private val repository: ItemRepository
) : ViewModel() {
    
    private val _uiState = MutableStateFlow(ItemListUiState())
    val uiState: StateFlow<ItemListUiState> = _uiState.asStateFlow()
    
    init {
        loadItems()
    }
    
    private fun loadItems() {
        viewModelScope.launch {
            _uiState.update { it.copy(isLoading = true) }
            try {
                val items = repository.getItems()
                _uiState.update { it.copy(items = items, isLoading = false) }
            } catch (e: Exception) {
                _uiState.update { it.copy(error = e.message, isLoading = false) }
            }
        }
    }
}
```

### Cross-Platform Development Patterns

**React Native with TypeScript**:
```typescript
interface User {
  id: string;
  name: string;
  email: string;
}

const UserProfile: React.FC<{ userId: string }> = ({ userId }) => {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const loadUser = async () => {
      try {
        const userData = await userService.getUser(userId);
        setUser(userData);
      } catch (error) {
        console.error('Failed to load user:', error);
      } finally {
        setLoading(false);
      }
    };

    loadUser();
  }, [userId]);

  if (loading) {
    return <LoadingSpinner />;
  }

  return (
    <View style={styles.container}>
      <Text style={styles.name}>{user?.name}</Text>
      <Text style={styles.email}>{user?.email}</Text>
    </View>
  );
};
```

**Flutter with Provider**:
```dart
class UserProvider extends ChangeNotifier {
  User? _user;
  bool _loading = false;
  
  User? get user => _user;
  bool get loading => _loading;
  
  Future<void> loadUser(String userId) async {
    _loading = true;
    notifyListeners();
    
    try {
      _user = await userService.getUser(userId);
    } catch (e) {
      _user = null;
    } finally {
      _loading = false;
      notifyListeners();
    }
  }
}

class UserProfileWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Consumer<UserProvider>(
      builder: (context, userProvider, child) {
        if (userProvider.loading) {
          return CircularProgressIndicator();
        }
        
        return Column(
          children: [
            Text(userProvider.user?.name ?? ''),
            Text(userProvider.user?.email ?? ''),
          ],
        );
      },
    );
  }
}
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
  - Main Prompt: `prompts/copilot/prompts/design-development/mobile-developer.md`
  - Examples: `rag/design-development/mobile-developer/examples.md`
  - Methodologies: `rag/design-development/mobile-developer/methodologies.md`
