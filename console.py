#!/usr/bin/python3
"""Command interpreter for the web app."""
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import re

classes = {
        "BaseModel": "BaseModel()",
        "User": "User()",
        "State": "State()",
        "City": "City()",
        "Place": "Place()",
        "Amenity": "Amenity()",
        "Review": "Review()"
}


class HBNBCommand(cmd.Cmd):
    """HBNB command line iterface."""

    prompt = "(hbnb) "

    def do_create(self, line=None):
        """Creates an instance of a class.

        Args:
            line: create parameter (class name)
        """
        if line is None:
            print("** class name missing **")
            return

        if line not in classes:
            print("** class doesn't exist **")
            return

        newModel = eval(classes[line])
        newModel.save()
        print(newModel.id)

    def do_show(self, line):
        """Prints string representation of an instance.

        Args:
            line: class name and instance name or id
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        if args[0] not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_dict = models.storage.all()
        key = str(args[0] + "." + args[1])
        if obj_dict.__contains__(key):
            print(obj_dict[key])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """Destroys an instance of an object.

        Args:
            line: arguments string
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        if args[0] not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_dict = models.storage.all()
        key = str(args[0] + "." + args[1])
        if obj_dict.__contains__(key):
            del obj_dict[key]
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line=None):
        """Prints string representation of all instance.

        Args:
            line: arguments string
        """
        obj_dict = models.storage.all()
        obj_list = []
        if len(line) == 0:
            for v in obj_dict.values():
                obj_list.append(v.__str__())

            print(obj_list)
        elif line in classes:
            for k, v in obj_dict.items():
                class_name = k.split('.')
                if line == class_name[0]:
                    obj_list.append(v.__str__())
            print(obj_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Update the content of an instance.
        Args:
            line: arguments string
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        if args[0] not in classes:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        if len(args) == 2:
            print("** attribute name missing **")
            return

        if len(args) == 3:
            print("** value missing **")
            return

        obj_dict = models.storage.all()
        key = str(args[0] + "." + args[1])

        if obj_dict.__contains__(key):
            obj = obj_dict[key]
            if args[2] in obj_dict.__class__.__dict__.keys():
                att_type = type(obj_dict.__class__.__dict__[args[2]])
                setattr(obj_dict[key], args[2], att_type(args[3]))
            else:
                setattr(obj_dict[key], args[2], args[3])
            models.storage.save()
        else:
            print("** no instance found **")

    def do_count(self, line):
        """Count the number of instances a class has."""
        count = 0

        if not line:
            print("** clas name missing **")
            return

        if line not in classes:
            print("** class doesn't exist **")
            return

        obj_dict = models.storage.all()
        for k, v in obj_dict.items():
            class_name = k.split('.')
            if line == class_name[0]:
                count += 1
        print(count)

    def default(self, line):
        """When input is not in predefined commands."""
        com_dict = {
                "all()": self.do_all,
                "count()": self.do_count
        }

        if re.search(r"\.", line) != None:
            com_key = line.split('.')
            for k, v in com_dict.items():
                if k == com_key[1]:
                    return v(com_key[0])
        print("*** Unknown syntax: {}".format(line))


    def do_quit(self, line):
        """Exits program.

        Args:
            line: command parameter
        """
        return True

    def do_EOF(self, line):
        """Exits program.

        Args:
            line: command parameter
        """
        return True

    def emptyline(self):
        """Does nothing (when no command is given)"""
        pass

    def help_create(self):
        """create command documentation."""
        print("Creates an instance of a class\n" +
              "Usage: create <class_name>\n")

    def help_show(self):
        """show command documentation."""
        print("Prints string representation of an instance\n" +
              "Usage: show <class_name> <instance_id>\n")

    def help_destroy(self):
        """destroy command documentation."""
        print("Deletes an instance of an object\n" +
              "Usage: destroy <class_name> <instance_id>\n")

    def help_all(self):
        """all command documentation."""
        print("Prints string representation of all or class" +
              " based instances\nUsage: all <class_name(optional)> or <class_name>.all()\n")

    def help_update(self):
        """upddate command documentation."""
        print("Update the attributes on an object based on class" +
              "\nUsage: update <class_name> <instance_id> <attribute name> <attribute value>\n")

    def help_count(self):
        """count command documentation."""
        print("Count the number of instances in a class" +
              "\nUsage: count <class_name> or <class_name>.count()\n")


    def help_quit(self):
        """quit command documentation."""
        print("Quits the console\n")

    def help_EOF(self):
        """EOF signal use documentation."""
        print("Quits the console\n")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
