#!/usr/bin/python3
"""
"""
import cmd
import shlex
import re
import ast
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = "(hbnb)"
    valid_class = ["BaseModel", "User", "Place", "City", "State", "Amenity", "Review"]

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        quit()

    def do_help(self, line):
        """
        """
        print("Quit command to exit the program")

    def emptyline(self):
        """Empty line command to do nothing\n"""
        pass

    def do_EOF(self, line):
        return True

    def do_create(self, line):
        cmd = shlex.split(line)
        if len(cmd) == 0:
            print("** class name missing **")
        elif cmd[0] not in self.valid_class:
            print("** class doesn't exist **")
        else:
            nw_instance = eval(f"{cmd[0]}()")
            storage.save()
            print(nw_instance.id)

    def do_show(self, line):
        """
        """
        cmd = shlex.split(line)
        if len(cmd) == 0:
            print("** class name missing **")
        elif cmd[0] not in self.valid_class:
            print("** class doesn't exist **")
        elif len(cmd) < 2:
            print("** instance id missing **")
        else:
            obj = storage.all()
            k = "{}.{}".format(cmd[0], cmd[1])
            if k in obj:
                print(obj[k])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        cmd = shlex.split(line)
        if len(cmd) == 0:
            print("** class name missing **")
        elif cmd[0] not in self.valid_class:
            print("** class doesn't exist **")
        elif len(cmd) < 2:
            print("** instance id missing **")
        else:
            obj = storage.all()
            k = "{}.{}".format(cmd[0], cmd[1])
            if k in obj:
                del obj[k]
                storage.save()
            else:
                print("** no instance found **")

    def default(self, line):
        """
        """
        lis_line = line.split('.')
        cls_nm_incoming = lis_line[0]
        cmd = lis_line[1].split('(')
        mth_incoming = cmd[0]
        extra_line_incomes = cmd[1].split(')')[0]

        mth_dic = {
            'show': self.do_show,
            'all': self.do_all,
            'update': self.do_update,
            'count': self.do_count,
            'destroy': self.do_destroy
        }
        if mth_incoming in mth_dic.keys():
            if mth_incoming != "update":
                return mth_dic[mth_incoming]("{} {}".format(cls_nm_incoming,
                                                            extra_line_incomes))
            else:
                if not cls_nm_incoming:
                    print("** class name missing **")
                    return
                try:
                    id_object, line_dic = self.curl_bra_split(extra_line_incomes)
                except Exception:
                    pass
                try:
                    return mth_dic[mth_incoming]("{} {} {}".format(cls_nm_incoming,
                                                                id_object,
                                                                line_dic))
                except Exception:
                    print("** argument missing **")

        print("*** Unknown syntax: {}".format(line))
        return False

    def curl_bra_split(self, extra_line_incomes):
        """
        """
        bra_curl = re.search(r"\{(.*?)\}", extra_line_incomes)
        if bra_curl:
            id_comma = shlex.split(extra_line_incomes[:bra_curl.span()[0]])
            id = [i.strip(",") for i in id_comma][0]
            data_stri = bra_curl.group(1)
            try:
                line_dic = ast.literal_eval("{" + data_stri + "}")
            except Exception:
                print("** invalid dictionary format **")
                return
            return id, line_dic
        else:
            cmd = extra_line_incomes.split(',')
            if cmd:
                try:
                    id = cmd[0]
                except Exception:
                    return "", ""
                try:
                    attr_name = cmd[1]
                except Exception:
                    return id, ""
                try:
                    attr_value = cmd[2]
                except Exception:
                    return id, attr_name
                return f"{id}", f"{attr_name} {attr_value}"

    def do_all(self, line):
        obj = storage.all()
        cmd = shlex.split(line)
        if len(cmd) == 0:
            for k, v in obj.items():
                print(str(v))
        elif cmd[0] not in self.valid_class:
            print("** class doesn't exist **")
        else:
            for k, v in obj.items():
                if k.split('.')[0] == cmd[0]:
                    print(str(v))

    def do_update(self, line):
        cmd = shlex.split(line)
        if len(cmd) == 0:
            print("** class name missing **")
        elif cmd[0] not in self.valid_class:
            print("** class doesn't exist **")
        elif len(cmd) < 2:
            print("** instance id missing **")
        else:
            obj = storage.all()
            k = "{}.{}".format(cmd[0], cmd[1])
            if k not in obj:
                print("** no instance found **")
            elif len(cmd) < 3:
                print("** attribute name missing **")
            elif len(cmd) < 4:
                print("**value missing **")
            else:
                o_obj = obj[k]
                bra_curl = re.search(r"\{(.*?)\}", line)
                if bra_curl:
                    data_stri = bra_curl.group(1)
                    line_dic = ast.literal_eval("{" + data_stri + "}")
                    attr_nms = list(line_dic.keys())
                    attr_vals = list(line_dic.values())
                    attr_name1 = attr_nms[0]
                    attr_val1 = attr_vals[0]
                    attr_name2 = attr_nms[1]
                    attr_val2 = attr_vals[1]
                    setattr(o_obj, attr_name1, attr_val1)
                    setattr(o_obj, attr_name2, attr_val2)
                else:
                    attr_name = cmd[2]
                    attr_value = cmd[3]
                    try:
                        attr_value = eval(attr_value)
                    except Exception:
                        pass
                    setattr(o_obj, attr_name, attr_value)
                    o_obj.save()

    def do_count(self, line):
        """
        """
        our_objs = storage.all()
        cmd = shlex.split(line)
        cnt = 0
        if line:
            cls_nm_incoming = cmd[0]

        if cmd:
            if cls_nm_incoming in self.valid_class:
                for obj in our_objs.values():
                    if obj.__class__.__name__ == cls_nm_incoming:
                        cnt += 1
                print(cnt)
            else:
                print("** invalid class name **")
        else:
            print("** class name missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
