clc
clear all
% close all

%% Signal with frequency F=100
Fs = 1200;                      % samples per second
dt = 1/Fs;                     % seconds per sample
StopTime = 0.03;                  % seconds
t = (0:dt:StopTime-dt)';
N = size(t,1);
   
f0 = 100;
f1 = 500;                       % hertz
f2 = 400;                       % hertz
x =  1*sin(2*pi*f0*t)+0.5*sin(2*pi*f1*t) + 0.3*sin(2*pi*f2*t);
X = fftshift(fft(x));
dF = Fs/N;                      % hertz
f = -Fs/2:dF:Fs/2-dF;           % hertz
figure;
subplot(2,1,1);
plot(t,x);
title('Input Signal');
subplot(2,1,2);
plot(f,abs(X)/N);
xlabel('Frequency (in hertz)');
title('Magnitude Response');
%% filter
% h =[-0.0085    0.0000    0.2451    0.5000    0.2451    0.0000   -0.0085];
% h= [-0.0023    0.0000    0.0054   -0.0000   -0.0159    0.0000    0.0385   -0.0000   -0.0893    0.0000    0.3124    0.5000    0.3124    0.0000   -0.0893   -0.0000   0.0385    0.0000   -0.0159   -0.0000    0.0054    0.0000   -0.0023];
h = [-0.0013    0.0000    0.0020   -0.0000   -0.0038    0.0000    0.0071   -0.0000   -0.0124    0.0000    0.0204   -0.0000   -0.0330    0.0000    0.0542   -0.0000   -0.1002    0.0000    0.3163    0.5000    0.3163    0.0000   -0.1002   -0.0000    0.0542    0.0000   -0.0330   -0.0000    0.0204    0.0000   -0.0124   -0.0000   0.0071    0.0000   -0.0038   -0.0000    0.0020    0.0000   -0.0013];

%% output
y11=conv(x,h);
l1=(length(h)-1)/2;
y1=y11(l1+1:end-l1);
figure
subplot(2,1,1)
plot(y1)
title('Output Signal of LPF');
Y1 = fftshift(fft(y1));
N_out1=N;
dF = Fs/N_out1;                      % hertz
f = -Fs/2:dF:Fs/2-dF;           % hertz
subplot(2,1,2)
plot(f,abs(Y1)/N_out1);
xlabel('Frequency (in hertz)');
title('Magnitude Response');

%% downsample
Fs_deci=Fs/2;
y=downsample(y1,2); % output of decimator is y
figure
subplot(2,1,1)
plot(y)
title('Output Signal of decimator');
Y = fftshift(fft(y));
N_out2=length(y);
dF = Fs_deci/N_out2;                      % hertz
f = -Fs_deci/2:dF:Fs_deci/2-dF;           % hertz
subplot(2,1,2)
plot(f,abs(Y)/N_out2);
xlabel('Frequency (in hertz)');
title('Magnitude Response');

%% Downsampler without LPF
Fs_deci=Fs/2;
x_d=downsample(x,2);
figure
subplot(2,1,1)
plot(x_d)
title('Output Signal of downsampler without LPF');
X_d = fftshift(fft(x_d));
N_out2=length(x_d);
dF = Fs_deci/N_out2;                      % hertz
f = -Fs_deci/2:dF:Fs_deci/2-dF;           % hertz
subplot(2,1,2)
plot(f,abs(X_d)/N_out2);
xlabel('Frequency (in hertz)');
title('Magnitude Response');