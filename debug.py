#!/usr/bin/env python

from plugin import Plugin

def main():
    plugin = Plugin("src/test/resources/test_param.json")
    plugin.initialize()
    plugin.run()
    
if __name__ == "__main__":
    main() 
