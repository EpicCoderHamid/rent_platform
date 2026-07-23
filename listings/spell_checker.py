# listings/spell_checker.py
import re
from difflib import SequenceMatcher

class SpellChecker:
    """Smart Spelling Mistake Handler"""
    
    # Common corrections dictionary
    CORRECTIONS = {
        # Electronics
        'iphne': 'iphone', 'iphon': 'iphone', 'i phone': 'iphone', 'iph0ne': 'iphone',
        'samsng': 'samsung', 'samsun': 'samsung', 'samsungg': 'samsung',
        'loptop': 'laptop', 'lapi': 'laptop', 'labtop': 'laptop', 'lappi': 'laptop',
        'mobail': 'mobile', 'moble': 'mobile', 'moblie': 'mobile',
        'headfone': 'headphone', 'headset': 'headphone',
        
        # Furniture
        'sfa': 'sofa', 'sofaa': 'sofa', 'sofe': 'sofa',
        'bedd': 'bed', 'tabel': 'table', 'tabl': 'table',
        'chaire': 'chair', 'cheer': 'chair', 'almari': 'wardrobe',
        
        # Vehicles
        'gari': 'car', 'gaari': 'car', 'kar': 'car', 'caar': 'car',
        'bik': 'bike', 'bikee': 'bike', 'motorcycel': 'motorcycle',
        'toyta': 'toyota', 'toyto': 'toyota', 'hond': 'honda', 'hondaa': 'honda',
        
        # Cities
        'labore': 'lahore', 'lhr': 'lahore', 'lahor': 'lahore', 'lhore': 'lahore',
        'krachi': 'karachi', 'khi': 'karachi', 'karach': 'karachi', 'karchi': 'karachi',
        'islambad': 'islamabad', 'isb': 'islamabad', 'islmabad': 'islamabad',
        'rawalpndi': 'rawalpindi', 'rwp': 'rawalpindi', 'pindi': 'rawalpindi',
        'multn': 'multan', 'mux': 'multan', 'fsd': 'faisalabad',
        
        # Price/Sort
        'sasta': 'cheap', 'sasty': 'cheap', 'sassta': 'cheap',
        'mehnga': 'expensive', 'mehngaa': 'expensive',
        'naya': 'newest', 'naye': 'newest', 'taza': 'newest', 'nwe': 'newest',
        'achha': 'good', 'acha': 'good', 'best': 'good',
        
        # General
        'and': '', 'for': '', 'the': '', 'a': '', 'an': '', 'in': '', 'on': '', 'at': '', 'to': '', 'with': '',
    }
    
    CITY_SHORTCUTS = {
        'khi': 'karachi', 'lhr': 'lahore', 'isb': 'islamabad',
        'rwp': 'rawalpindi', 'mux': 'multan', 'fsd': 'faisalabad',
        'grw': 'gujranwala', 'pew': 'peshawar', 'uqt': 'quetta',
    }
    
    @classmethod
    def get_similarity(cls, word1, word2):
        """Get similarity percentage between two words"""
        return SequenceMatcher(None, word1.lower(), word2.lower()).ratio() * 100
    
    @classmethod
    def correct_word(cls, word):
        """Correct a single word"""
        word_lower = word.lower()
        
        # Direct correction
        if word_lower in cls.CORRECTIONS:
            return cls.CORRECTIONS[word_lower]
        
        # City shortcut
        if word_lower in cls.CITY_SHORTCUTS:
            return cls.CITY_SHORTCUTS[word_lower]
        
        # Fuzzy matching for close words
        all_words = list(cls.CORRECTIONS.keys()) + list(cls.CITY_SHORTCUTS.keys())
        best_match = None
        best_score = 0
        
        for dict_word in all_words:
            score = cls.get_similarity(word_lower, dict_word)
            if score > best_score and score >= 50:
                best_score = score
                best_match = dict_word
        
        if best_match:
            if best_match in cls.CORRECTIONS:
                return cls.CORRECTIONS[best_match]
            if best_match in cls.CITY_SHORTCUTS:
                return cls.CITY_SHORTCUTS[best_match]
        
        return word
    
    @classmethod
    def correct_query(cls, query):
        """Correct entire search query"""
        if not query:
            return query, False
        
        words = query.split()
        corrected_words = []
        changed = False
        
        for word in words:
            corrected = cls.correct_word(word)
            if corrected != word:
                changed = True
            corrected_words.append(corrected)
        
        return ' '.join(corrected_words), changed
    
    @classmethod
    def get_suggestions(cls, query, max_suggestions=3):
        """Get search suggestions"""
        words = query.split()
        suggestions = []
        
        for word in words:
            if word.lower() not in cls.CORRECTIONS:
                all_words = list(cls.CORRECTIONS.keys())
                for dict_word in all_words:
                    score = cls.get_similarity(word.lower(), dict_word)
                    if score >= 60:
                        suggestions.append(cls.CORRECTIONS[dict_word])
        
        return list(set(suggestions))[:max_suggestions]