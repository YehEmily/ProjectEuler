function div = Euler12divisors(n)


FactorNumber = factor(n);
UniqueFactors = unique(FactorNumber);
HistogramCount = histc(FactorNumber,UniqueFactors);


vec = (UniqueFactors(1)).^(0:HistogramCount(1));


for i=2:length(UniqueFactors)
    fac = UniqueFactors(i);
    x = fac.^(0:HistogramCount(i));
    vec = kron(vec,x);
end


div = sort(vec);