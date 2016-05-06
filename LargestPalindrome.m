% A palindromic number reads the same both ways. The largest palindrome made
% from the product of two 2-digit numbers is 9009 = 91 × 99.
% 
% Find the largest palindrome made from the product of two 3-digit numbers.

x1 = 100:999;
x2 = 100:999;
f=zeros(1,900^2);
for i = x1.*x2
%     if length(num2str(i)) == 3
    string = num2str(i);
    if string == fliplr(string)
        f(i) = i;
%     end
    end
end

max(f)