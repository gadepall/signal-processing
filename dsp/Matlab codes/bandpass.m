clc;
clear all;
close all;

fc1 = 500;
fs1 = 6000;
wc1 = 2*pi*fc1/fs1;
fc2 = 1200;
wc2 = 2*pi*fc2/fs1;

N = 39;
alpha = (N-1)/2;
n = 0:1:N-1;

hd = (sin(wc2*(n-alpha))-sin(wc1*(n-alpha)))./(pi*(n-alpha));
hd(alpha+1) = (wc2-wc1)/pi;

%wr = boxcar(N);
wr=hamming(N);
%wr=hann(N);
%wr= bartlett(N)
hn = hd.*wr';
w = 0:0.01:pi;
Hz = freqz(hn,1,w);
%plot(w/pi,abs(Hz));
fvtool(hn,1)
% freqz(hn)
