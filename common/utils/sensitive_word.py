#!/usr/bin/env python
# -*- coding:utf-8 -*-
# project : TextSafeApi
# filename : sensitive_word
# author : ly_13
# date : 8/9/2023


import os


class SensitiveWords(object):
    """
    敏感词处理
    从文件中读取敏感词,添加不同类别的敏感词,保存到txt或者DB中

    # >>>s = SensitiveWords()
    # >>>s.get_sensitive_word('./data/SensitiveWords/ad.txt') # 读取文件中的敏感词,要求数据每个一行
    # >>>s.add_sensitive_word('default')                     # 添加敏感词 <unicode>
    # >>>s.add_sensitive_word('minitrill', word_type='ad')    # 添加敏感词 str 并指定敏感词类型
    # >>>s.save_data()                                        # 保存敏感词数据
    # >>>s.sensitive_word_dict                                # 核心数据被保存在字典中
    """

    # Singleton
    _instance = None

    def __new__(cls, *args, **kw):
        """单例模式"""
        if not cls._instance:
            cls._instance = super(SensitiveWords, cls).__new__(cls, *args, **kw)
        return cls._instance

    def __init__(self):
        """构造函数:读取敏感词文件并初始化字典"""
        base_path = os.path.dirname(os.path.dirname(__file__))
        self.sensitive_words_data_path = os.path.join(base_path, 'data')  # 敏感词数据文件(要求一类数据一个txt文件)
        self.file_name_list = os.listdir(self.sensitive_words_data_path)
        self.file_path_list = map(lambda file_name: os.path.join(self.sensitive_words_data_path, file_name),
                                  self.file_name_list)
        self.sensitive_word_dict = {}
        for file_path in self.file_path_list:
            self.get_sensitive_word(file_path)

    def __str__(self):
        """输出敏感词类详细信息"""
        result = f"共 {len(self.sensitive_word_dict.keys())} 类 ({','.join(self.sensitive_word_dict.keys())})类敏感词:\n"
        for k in self.sensitive_word_dict.keys():
            result += k + "\t-\t" + str(len(self.sensitive_word_dict[k])) + " 个 \n"
        return result

    def get_sensitive_word(self, file_path):
        """从文件中读取敏感词(每个一行)"""
        with open(file_path, 'rb') as f:
            sensitive_word_type = os.path.basename(file_path).replace('.txt', '')
            self.sensitive_word_dict[sensitive_word_type] = []
            for line in f:
                if line.strip():
                    word = line.strip().decode('utf-8')
                    self.sensitive_word_dict[sensitive_word_type].append(word)

    def add_sensitive_word(self, word, word_type='default', word_weight='10'):
        """添加敏感词"""
        if word_type in self.sensitive_word_dict.keys() or word_type == 'default':
            self.sensitive_word_dict[word_type][word] = word_weight


#     def save_data(self):
#         """存储数据到文件中(读取地址)"""
#         for word_type in self.sensitive_word_dict.keys():
#             file_path = filter(lambda x: word_type in x, self.file_path_list)
#             with open(file_path, 'wb') as f:
#                 for word in self.sensitive_word_dict[word_type]:
#                     f.write(word.encode("utf-8"))
#                     f.write("\n")
#
#
# if __name__ == '__main__':
#     s = SensitiveWords()
#     s.save_data()

sensitive_words = SensitiveWords()
