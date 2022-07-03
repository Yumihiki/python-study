from dataclasses import dataclass


@dataclass
class Name:
    """名前クラス"""
    firstname: str
    lastname: str

    def __post_init__(self):
        """ガード節"""
        if self.firstname == '':
            raise ValueError(f"空文字の入力はNGです")
        if self.lastname == '':
            raise ValueError(f"空文字の入力はNGです")

    def call_name(self):
        print(f'{self.lastname} {self.firstname}')


if __name__ == "__main__":
    true_name = Name('Kiyoshiro', 'YUMEMIZU')
    true_name.call_name()

    # __post_init__ で空文字NGのチェックを行っているため
    # インスタンス生成時にValueErrorを発生させることができる
    raise_name = Name('Yumihiki', '')
    raise_name.call_name()
