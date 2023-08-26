clc
clear all
close all
%% LPF with fc =300(continious time cutoff freq)
fc=300;
f=1200;
w=2*pi*fc/f;
N=39;

for k=-(N-1)/2:(N-1)/2
    if k==0
        hd(k+(N+1)/2)=w/pi;
    else
        hd(k+(N+1)/2)=sin(w*k)/(k*pi);
    end
end

 w1=boxcar(N);
w2=hamming(N);
 w3=hann(N);
 w4=bartlett(N);

 h1=hd.*w1';
h2=hd.*w2';
 h3=hd.*w3';
 h4=hd.*w4';

% fvtool(h1,1);
%freqz(h1);
fvtool(h2,1);
% fvtool(h3,1);
% fvtool(h4,1);
