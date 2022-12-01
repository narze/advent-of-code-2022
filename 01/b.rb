p `cat input.txt`.lines.slice_when { _2 == "\n" }.map { _1.sum(&:to_i) }.sort.last(3).sum
