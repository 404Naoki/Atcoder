n = gets.to_i

ans = n / 100

if(n % 100 != 0)
  ans += 1
end

puts ans