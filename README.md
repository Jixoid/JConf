## 🧩 JConf

JConf is a lightweight and extensible configuration format designed for embedded systems, operating systems, and low-level tooling. It supports both human-readable text syntax and compact binary representation, making it ideal for flexible deployment scenarios.


## 📝 Syntax

The syntax of JConf is minimal and deterministic. It uses a key-value pair structure with support for nested sections, arrays, and typed values. Example:

```
System: {
  Name: "QAOS"
  Version: 1
  Modules: [ "core", "net", "ui" ]
}
```

The same structure can be serialized into a binary format for efficient parsing and loading.


## 🚧 Status

JConf is under active development. The core parser and binary serializer are functional, but the schema validator and advanced tooling are in progress. Expect breaking changes as the format evolves.


## 🤝 Contributions

Contributions are welcome, especially around:

    Parser/serializer improvements

    Schema validation

    Language bindings

    Tooling (editors, linters, etc.)

Suggested workflow:

    Fork the repository

    Create a feature branch (feature/your-idea)

    Commit and push your changes

    Open a pull request


## 📜 License

JConf project uses multiple licenses:

- GPL for **source code**.
- LGPL for **build system**.

Please see the `LICENSE` file for detailed information.
You can find the license texts in the `LICENSES` folder.
