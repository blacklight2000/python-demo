def p_decorator(func):
   def func_wrapper(*args, **kwargs):
       return "<p>Greetings, {0}</p>".format(func(*args, **kwargs))
   return func_wrapper

class Person(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @p_decorator
    def get_name(self):
        return self.first_name+" "+self.last_name

the_person = Person("Anne","Grifo")

print the_person.get_name()

