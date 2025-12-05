# JConf C++ API Reference

The C++ API wraps the C API in a safe, easy-to-use `jconf::Value` class.

`#include "jconf/JConf.hh"`

`using namespace jconf;`


## class jconf::Value

### Constructors

- `Value()` - Null.
- `Value(int/long/long long)` - Integer value.
- `Value(bool)` - Boolean value.
- `Value(const char* / string)` - String value.
- `Value(data_64)` - Binary data.
- `Value(initializer_list<Value>)` - Array.

Copy and Move semantics are fully supported.


### Type Checks
- `bool isNull() const;`
- `bool isInt() const;`
- `bool isBool() const;`
- `bool isString() const;`
- `bool isData() const;`
- `bool isStruct() const;`
- `bool isArray() const;`


### Accessors (Casting)
- `operator int()`
- `operator i64()`
- `operator bool()`
- `operator string()`
- `operator data_64()`


### Struct Operations
- `Value get(const string& Key) const;`
- `void set(const string& Key, const Value& Val);`
- `Value operator[](const string& Key) const;`
- `u32 size() const;`


### Array Operations
- `Value at(u32 Index) const;`
- `void push(const Value& Val);`
- `Value operator[](int Index) const;`
- `u32 size() const;`


### Static Methods (Parsing)
- `static Value Parse(const string& Path);` - Auto-detect format.
- `static Value ParseRaw(const string& Path);` - Parse text.
- `static Value ParseBin(const string& Path);` - Parse binary.


### I/O Methods
- `void saveRaw(const string& Path) const;` - Save as text.
- `void saveBin(const string& Path) const;` - Save as binary.


## Example

```cpp
#include "jconf/JConf.hh"
using namespace jconf;

int main() {
    // Parsing
    Value config = Value::Parse("config.jconf");
    
    // Accessing
    string name = config["System"]["Name"];
    int version = config["System"]["Version"];
    
    // Creating
    Value newConfig;
    newConfig.set("User", "Alforce");
    newConfig.set("Active", true);
    
    // Arrays
    Value list = { 1, 2, 3 };
    newConfig.set("List", list);
    
    // Saving
    newConfig.saveRaw("new_config.jconf");
}
```
