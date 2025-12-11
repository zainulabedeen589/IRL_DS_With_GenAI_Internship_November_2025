class Solution:
    def defangIPaddr(self, address: str) -> str:
        """
        Replaces every period "." in the IP address with "[.]".

        :param address: A valid IPv4 address string (e.g., "192.168.1.1").
        :return: The defanged version of the IP address (e.g., "192[.]168[.]1[.]1").
        """

        # --- Method 1: Using the built-in string replace method ---
        # This is the most idiomatic and Pythonic way to solve this.
        # The .replace() method will find all occurrences of the first argument
        # and substitute them with the second argument.
        return address.replace(".", "[.]")

        # --- Alternative Method 2: Using a loop (More manual approach) ---
        # defanged_address = ""
        # for char in address:
        #     if char == '.':
        #         defanged_address += "[.]"
        #     else:
        #         defanged_address += char
        # return defanged_address

        # --- Alternative Method 3: Using string joining (Conceptually similar to loop) ---
        # The split('.') function breaks the address into a list of components
        # (e.g., "1.1.1.1" becomes ["1", "1", "1", "1"]).
        # The join('[.]') then rejoins these components using "[.]" as the separator.
        # return "[.]".join(address.split('.'))
