"""
整数の配列を昇順にソートするアルゴリズム

input: 整数のランダムに並んだ配列
output: 整数の昇順に並んだ配列

"""

def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    left_index = 0
    right_index = len(array) - 1

    while left_index < right_index: # 先頭と末端の検索がぶつかるまで処理を続行
        # 先頭から基準値以上の値を探す
        if array[left_index] < pivot:
            left_index += 1
            continue
        # 末端から基準値未満の値を探す
        if array[right_index] >= pivot:
            right_index -= 1
            continue
        # 先頭から探した基準値以上の値と、末端から探した基準値未満の値どちらも見つかったら入れ替える
        array[left_index], array[right_index] = array[right_index], array[left_index]

    # 配列がすでに昇順に並んでいた場合は、そのまま返却
    if right_index == 0:
        return array

    # 基準値以上と基準値未満のグループに分ける   
    left_arr = array[:left_index]
    right_arr = array[left_index:]

    # 左右２つに分割したリストに対して、再帰的に関数を呼び出して繰り返す
    left_arr = sort(left_arr)
    right_arr = sort(right_arr)

    # ソートしたら分割したリストを結合
    return left_arr + right_arr


if __name__ == '__main__':
    main()
