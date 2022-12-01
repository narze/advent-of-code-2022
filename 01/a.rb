p File.open('input.txt').slice_when { _2 == "\n" }.map { _1.sum(&:to_i) }.max
