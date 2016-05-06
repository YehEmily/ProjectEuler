% 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
% 
% What is the sum of the digits of the number 2^1000?

A = '35356536576821';
A = char(regexp(A,'\d+','match'));
while ~isscalar(A)
    A = num2str(sum(A - '0'));
end