from typed_argument_parsing import TypedArgumentParser


class MyArgumentParser(TypedArgumentParser):
    """My way better argument parser.

    Attributes:
    :data_path: Path to data file.
        One that is very important!

        An unusually cool path.
    :embedding_path: Path to embedding file.
    :hidden_size: Hidden size.
    """
    data_path: str
    embedding_path: str = '/home'
    hidden_size: int = 2

    def add_arguments(self) -> None:
        self.add_argument('-dp', '--data_path', required=True)
        self.add_argument('--embedding_path')
        self.add_argument('--hidden_size')


if __name__ == '__main__':
    parser = MyArgumentParser()
    args = parser.parse_args()

    print(args.data_path)
    print(args.embedding_path)
    print(args.hidden_size)
