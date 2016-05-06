% A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
% 
% a2 + b2 = c2
% For example, 32 + 42 = 9 + 16 = 25 = 52.
% 
% There exists exactly one Pythagorean triplet for which a + b + c = 1000.
% Find the product abc.

for a = 1:1000
    for b = 2:1000
            for c = 3:1000
                if a < b
                    if b < c
                        if (a^2 + b^2) == c^2
                            if (a + b + c) == 1000
                                P = [a b c]
                            end
                    end
                end
            end
       end
    end
end