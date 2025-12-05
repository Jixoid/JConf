# JConf C API Reference

  
The C API provides a low-level interface for creating, manipulating, and parsing JConf structures.

`#include "jconf/JConf.h"`

  
## Types

- `jc_obj;`
- `jc_val;` // String
- `jc_int;` // Integer (64-bit)
- `jc_bool;` // Boolean
- `jc_data;` // Binary Data
- `jc_stc;` // Object/Struct
- `jc_arr;` // Array

  
## Error Handling

### Error Codes

```c
const u32
	JC_ERR_OK = 0,
	JC_ERR_InternalError = 1,
	JC_ERR_FileNOpened = 2,
	JC_ERR_FileIsCorrupt = 3,
	JC_ERR_InvalidIdentifier = 4,
	JC_ERR_UnexpectedWord = 5,
	JC_ERR_InvalidValue = 6,
	JC_ERR_ConvertToInteger = 7,
	JC_ERR_NestedOverflow = 8;
```

  
### Functions

- `u32 jc_err_get();` - Get the last error code and reset it to `JC_ERR_OK`.
- `const char* jc_err_str();` - Get the string representation of the last error.


## Parsing  

- `jc_stc jc_parse(const char* fpath);` - Auto-detect format (Binary/Text) and parse file.
- 
- `jc_stc jc_parse_raw(const char* fpath);` - Parse text file.
- `jc_stc jc_parse_bin(const char* fpath);` - Parse binary file.


## Writing

- `void jc_write_raw(const char* fpath, jc_stc data);` - Write structure to text file.
- `void jc_write_bin(const char* fpath, jc_stc data);` - Write structure to binary file.


## Type Checking  

- `bool jc_is_val(jc_obj);`
- `bool jc_is_int(jc_obj);`
- `bool jc_is_bool(jc_obj);`
- `bool jc_is_data(jc_obj);`
- `bool jc_is_stc(jc_obj);`
- `bool jc_is_arr(jc_obj);`


## Object Creation

- `jc_val jc_new_val(char* value);`
- `jc_int jc_new_int(u64 value);`
- `jc_bool jc_new_bool(bool value);`
- `jc_data jc_new_data(data_64 value);`
- `jc_stc jc_new_stc();`
- `jc_arr jc_new_arr(jc_obj value[], u32 count);`


## Memory Management

- `void jc_dis_obj(jc_obj obj);` - Destroy object and free memory.

- `jc_obj jc_copy(jc_obj);` - Deep copy object.


## Getters & Setter

### Value (String)

- `const char* jc_val_get(jc_val);`
- `void jc_val_set(jc_val, const char* value);`

### Integer

- `i64 jc_int_get(jc_int);`
- `void jc_int_set(jc_int, i64 value);`

### Boolean

- `bool jc_bool_get(jc_bool);`
- `void jc_bool_set(jc_bool, bool value);`

### Data

- `data_64 jc_data_get(jc_val);`
- `void jc_data_set(jc_val, data_64 value);`

### Struct

- `jc_obj jc_stc_get (jc_stc, const char* scope);`
- `void jc_stc_set (jc_stc, const char* scope, jc_obj object);`
- `void jc_stc_del (jc_stc, const char* scope);`
- `u32 jc_stc_count(jc_stc);`
- `jc_obj jc_stc_index(jc_stc, u32 index, char** Name);`
- `void jc_stc_clear(jc_stc);`

### Array

- `jc_obj jc_arr_get (jc_arr, u32 index);`
- `void jc_arr_set (jc_arr, u32 index, jc_obj object);`
- `u32 jc_arr_count(jc_arr);`
- `void jc_arr_push (jc_arr, jc_obj object);`
- `void jc_arr_pushl(jc_arr, jc_obj value[], u32 count);`
- `void jc_arr_del (jc_arr, u32 index);`
- `void jc_arr_clear(jc_arr);`

