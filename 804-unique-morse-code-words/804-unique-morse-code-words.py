class Solution(object):
    def uniqueMorseRepresentations(self, words):
        morse_code = {"a":".-", "b":"-...", "c":"-.-.", "d":"-..", "e":".", "f":"..-.", "g":"--.", "h":"....", "i":"..", "j":".---", "k":"-.-", "l":".-..", "m":"--", "n":"-.", "o":"---", "p":".--.", "q":"--.-", "r":".-.", "s":"...", "t":"-", "u":"..-", "v":"...-", "w":".--", "x":"-..-", "y":"-.--", "z":"--.."}
        
        encoding = []
        
        for word in words:
            morse = ""
            
            for w in word:
                morse += morse_code[w]
                
            encoding.append(morse)
            
        return len(set(encoding))
            
        