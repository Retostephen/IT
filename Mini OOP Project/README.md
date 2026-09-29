# Week 7 - OOP Mini Project: Inventory Management System

## Objective
Consolidate concepts from earlier assignments (functions, dictionaries,
file handling) under an object-oriented design, using classes to bundle
data and behavior together instead of passing data between standalone
functions.

## Description
A command-line inventory tracker built with two classes:

- **`Item`** — represents a single inventory item (name, quantity, price)
  and can calculate its own total value.
- **`Inventory`** — manages a collection of `Item` objects. Supports
  adding, removing, searching, and updating items, and calculates the
  total value of all stock.

Inventory data is saved to and loaded from a plain text file
(`inventory_data.txt`) through the `Inventory` class's own methods
(`save_to_file` / `load_from_file`), so records persist between runs.

## How to Run
```bash
python3 inventory_system.py
```
Follow the on-screen menu to add, remove, search, update, or view items.
Choosing option 6 saves the current inventory to `inventory_data.txt`
before exiting.
