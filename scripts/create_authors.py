from pathlib import Path


def gen_content(name: str, item: str) -> str:
    first, second = name.title().split('-')

    content = '---\n'
    content += f'title: {first} {second}\n'
    content += f'authors:\n'
    content += f'- {name}\n'
    content += f'role: {item}\n'
    content += f'user_groups:\n'
    content += f'- {item}\n'
    content += '---\n'
    return content


def create_all_authors():
    all_authors = {
        'Researchers': ['shanshe-wang', 'chuanmin-jia'],
        'Collaboration': ['xinfeng-zhang', 'shiqi-wang', 'jian-zhang', 'wei-gao'],
        'Ph.D Students': [
            # 15
            'yunlong-li', 'zhenhua-liu', 'yiqun-xu',
            # 16
            'jiguo-li',
            # 17
            'suhong-wang', 'jiaqi-zhang', 'tianliang-fu', 'xuewei-meng', 'yuhuai-zhang',
            'yuqing-zhang', 'xu-han', 'junlong-gao', 'yang-li',
            # 18
            'meng-lei', 'kai-lin', 'zheng-chang', 'haopeng-lu',
            # 19
            'zhimeng-huang', 'wenhong-duna', 'huiwen-ren', 'wenkang-shan',
            # 20
            'ziqing-ge', 'yanchen-zhao',
            # 21
            'qi-zhang', 'qian-yin', 'jianhui-chang', 'ruoke-yan', 'kexiang-feng',
        ],
        'Master Students': [
            'yuefeng-zhang',  # 18
            'jijun-shi',  # 19
            'ruofan-wang',  # 20
        ],
        'Intern Students': [
            'xinyu-hang', 'zetian-song', 'yizhao-wang', 'dongjie-lu'
        ]
    }

    for item, names in all_authors.items():
        for name in names:
            author_dir = Path(f'./content/authors/{name}')
            if not author_dir.exists():
                author_dir.mkdir()
                author_path = author_dir / '_index.md'
                author_path.write_text(gen_content(name, item), encoding='utf-8')
                print(item, name, 'created')


if __name__ == '__main__':
    create_all_authors()