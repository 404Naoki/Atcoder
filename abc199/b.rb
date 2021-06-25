n = gets.to_i
a = gets.split.map(&:to_i)
b = gets.split.map(&:to_i)

mx = a.max
mn = b.min

puts (mn - mx + 1) > 0 ? mn - mx + 1 : 0