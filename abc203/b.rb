n, k = gets.split.map(&:to_i)

ans = 0

for i in 1..n do
  for j in 1..k do
    ans += (i * 100) + j
  end
end

puts(ans)