def cheby (x1, y1, x2, y2){
  return max((x1 - x2).abs, (y1 - y2).abs);
}

n = gets.to_i

xs = []
ys = []

n.times do
  x, y = gets.to_s.split.map{ |e| e.to_i }
  xs += x
  ys += y
end

chebList = []
