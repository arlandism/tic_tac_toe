class HashTransformer(object):

      @staticmethod
      def try_dict_key_conversion(dictionary):
          new_dict = {}
          try:
            for orig_key,val in dictionary.items():
                converted_key = HashTransformer.try_int_conversion(orig_key)
                if HashTransformer.is_terminal(dictionary,orig_key):
                    new_dict[converted_key] = val
                else:
                    converted_val = HashTransformer.try_dict_key_conversion(val)
                    new_dict[converted_key] = converted_val
            return new_dict
          except:
              return dictionary

      @staticmethod
      def try_int_conversion(key):
          try:
              key = int(key)
          except:
              pass
          return key

      @staticmethod
      def is_terminal(dictionary,key):
          type_key_maps_to = type(dictionary[key])
          return not(type_key_maps_to == dict)
