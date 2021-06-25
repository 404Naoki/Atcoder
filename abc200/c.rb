n = gets.to_i
a = gets.split.map(&:to_i)

n.times do |i|
  a[i] %= 200;
end

cnt = Array.new(5000001, 0)

a.reverse

ans = 0
n.times do |i|
  ans += cnt[a[i]]
  cnt[a[i]] += 1
end

puts ans