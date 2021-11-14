#!/usr/bin/python3

import unittest
import models
from models.engine.file_storage import FileStorage
from models.__init__ import storage
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User


class TestAirbnb_Storage(unittest.TestCase):
    """ test to class FileStorage """

    def test_fs_class(self):
        """ test the class of FileStorage """
        fs = FileStorage()

        self.assertEqual(fs.__class__, FileStorage)

    def test_fs_storage(self):
        """ test the class of storage """
        self.assertTrue(isinstance(models.storage, FileStorage))

    def test_fs_all(self):
        """ test existence class methods """
        fs = FileStorage()

        self.assertTrue(hasattr(fs, 'all'), True)

    def test_fs_new(self):
        """ test existence class methods """
        fs = FileStorage()

        self.assertTrue(hasattr(fs, 'new'), True)

    def test_fs_save(self):
        """ test existence class methods """
        fs = FileStorage()

        self.assertTrue(hasattr(fs, 'save'), True)

    def test_fs_reload(self):
        """ test existence class methods """
        fs = FileStorage()

        self.assertTrue(hasattr(fs, 'reload'), True)

    def test_exe_all(self):
        """ test methods """
        self.assertEqual(type(models.storage.all()), dict)

    def test_new_instance(self):
        """ test the creation of different instances """
        b = BaseModel()
        s = State()
        c = City()
        a = Amenity()
        p = Place()
        r = Review()
        u = User()
            
        models.storage.new(b)
        models.storage.new(s)
        models.storage.new(c)
        models.storage.new(a)
        models.storage.new(p)
        models.storage.new(r)
        models.storage.new(u)

        self.assertIn('{}.{}'.format(b.__class__.__name__, b.id), models.storage.all().keys())
        self.assertIn('{}.{}'.format(s.__class__.__name__, s.id), models.storage.all().keys())
        self.assertIn('{}.{}'.format(c.__class__.__name__, c.id), models.storage.all().keys())
        self.assertIn('{}.{}'.format(a.__class__.__name__, a.id), models.storage.all().keys())
        self.assertIn('{}.{}'.format(p.__class__.__name__, p.id), models.storage.all().keys())
        self.assertIn('{}.{}'.format(r.__class__.__name__, r.id), models.storage.all().keys())
        self.assertIn('{}.{}'.format(u.__class__.__name__, u.id), models.storage.all().keys())
       
