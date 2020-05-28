#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
try:
    import requests
except ImportError as err:
    print('ERROR : requests module is not installed - cannot continue !\n requests library can be installed using "pip install requests"')
    sys.exit(1)

class HTTPRequest:
    def __init__(self, url):
        """
        HTTPRequest class has methods that can be used to
        send requests using Python's requests library
        :param url: URL to send HTTP request and fetch response
        """
        self.url = url

    def send_http_get_req(self):
        """
        Send HTTP GET Request to given url and returns the website response
        :return: HTTP Response
        """
        print("INFO - Sending HTTP GET Req to ({}) ".format(self.url))
        request = requests.get(url=self.url)
        if request.status_code == 200 or request.status_code == 204:
            print('SUCCESS - Request to ({}) succeeded with status_code ({})'.format(self.url,request.status_code))
            print('SUCCESS - Response  ({})'.format(request.text))
        else:
            print('ERROR - Request to ({}) failed with status_code ({})'.format(self.url, request.status_code))
        return request.text

class BigramVector:
    def __init__(self, text: str):
        """
        BigramVector is a class that can be used
        to compute bigram-vector for any given string
        :param text: Text string for which to compute bigram_vetor
        """
        self.text = text

    def compute_bigram_dictionary(self):
        """
        Function to compute bigram dictionary from the text
        :return: Bigram Dictionary for self.text
        """
        dicts = {}
        for i in range(len(self.text) - 1):
            s = self.text[i:i + 2]
            if s in dicts:
                dicts[s] = dicts[s] + 1
            else:
                dicts[s] = 1
        return dicts

    @staticmethod
    def __indexing(character):
        """
        Private Helper method to get the indexing of the character
        :param character:
        :return: returns indexing of the character
        """
        char1 = hex(ord(character[0]))
        char2 = hex(ord(character[1]))
        result = char1[2:] + char2[2:]
        return int(result, 16)

    def feature_vector(self):
        """
        Get the transformed vector from the bigram dictionary
        :return: Feature Vector for self.text
        """
        feature_vector = {}
        sorted_feature_vector = []
        bigram_dictionary = self.compute_bigram_dictionary()
        for x in bigram_dictionary:
            feature_vector[self.__indexing(x)] = bigram_dictionary[x]
        for k in sorted(feature_vector):
            sorted_feature_vector.append("{key}:{value}".format(key=k,value=feature_vector[k]))
        return " ".join(sorted_feature_vector)

def tester(tests:dict):
    """
    Tester function to test feature vector code.
    :param tests: Key: Value pair of (text,expected_feature_vector)
    :return: True if matches, False otherwise
    """
    for text,expected_fv in tests.items():
        b_obj = BigramVector(text=text)
        fv = b_obj.feature_vector()
        assert fv == expected_fv, "Feature Vectors didn't match -> Expected Feature Vector : {}, Got Feature Vector : {}".format(expected_fv,fv)
    print('SUCCESS : ALL Tests PASSED')

def main():
    # 1. Get the url content
    http_client = HTTPRequest(url="https://pastebin.com/raw/V5XpP3s0")
    response = http_client.send_http_get_req()
    # 2. Create bigram_vector object
    bigram_vector_object = BigramVector(text=response)
    # 3. Get the Bigram Dictionary
    bigram_dictionary = bigram_vector_object.compute_bigram_dictionary()
    # 4. Get the Feature Vector
    feature_vector = bigram_vector_object.feature_vector()
    print('The Bigram Dictionary is : {}'.format(bigram_dictionary))
    print('The Feature Vector is : {}'.format(feature_vector))
    print('='*150)
    # 5. Testing for other inputs
    unit_tests = {
                    "hahahaha" : "24936:3 26721:4",
                    "banana" : "24942:2 25185:1 28257:2",
                    "do or do not":"8292:1 8302:1 8303:1 25711:2 28271:1 28448:2 28530:1 28532:1 29216:1"
    }
    tester(unit_tests)

if __name__ == '__main__':
    main()


# In[ ]:





# In[ ]:




