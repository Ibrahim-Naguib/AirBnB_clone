# AirBnb Clone - The console

## Description

This project is an implementation of a command-line interface (CLI) for an Airbnb clone. The Airbnb clone aims to replicate some of the core functionalities of the popular accommodation rental platform Airbnb, allowing users to manage and interact with properties, users, and bookings through a text-based interface.

#### How to Start

To start the Airbnb clone console, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/AirBnB_clone
   ```

2. Navigate to the cloned repository:

   ```bash
   cd AirBnB_clone
   ```

3. Run the command interpreter:

   ```bash
   python3 console.py
   ```

   or

   ```bash
   ./console.py
   ```

##### How to Use

Once the command interpreter is running, you can start entering commands to interact with the Airbnb clone. Here are some examples of commands you can use:

- `create <object>`: Create a new object (e.g., user, property, booking).
- `show <object> <id>`: Show details of a specific object.
- `update <object> <id>`: Update the details of an existing object.
- `destroy <object> <id>`: Delete an object.
- `all <object>`: Show all objects of a specific type.
- `quit` or `EOF`: Exit the command interpreter.

For a complete list of commands and their usage, refer to the documentation or use the `help` command within the console.

###### Examples

1. Creating a new user:

   ```bash
   (hbnb) create User
   ```

2. Showing details of a specific user:

   ```bash
   (hbnb) show User 0e162295-2807-45f1-90d8-e75c5543013b
   ```

3. Updating the details of an existing user:

   ```bash
   (hbnb) update User 0e162295-2807-45f1-90d8-e75c5543013b first_name John
   ```

4. Deleting an object:

   ```bash
   (hbnb) destroy User 0e162295-2807-45f1-90d8-e75c5543013b
   ```

5. Showing all users:

   ```bash
   (hbnb) all User
   ```

6. Exiting the command interpreter:

   ```bash
   (hbnb) quit
   ```
