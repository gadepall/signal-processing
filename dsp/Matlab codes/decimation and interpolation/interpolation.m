%% Interpolation using half band filter
% CSP LAB (Aug-Dec, 2019) Demo

% clear command window, workspace, close figures
% clc;
clear;
close all;

% input signal
% t = 0:.2:6*pi; % time
% t_alt = t(1:2:end);
% input = sin(t_alt);


%7 tap
% input=[0.2348    0.6976    0.8298   -0.0000   -0.8298   -0.7062   -0.0000    0.7062    0.8298    0.0000   -0.8298   -0.7062    0.0000    0.7062    0.8298   -0.0000   -0.8298   -0.6976];
%23 tap
% input=[0.2024    0.8241    0.8821   -0.0091   -0.8612   -0.8658   -0.0000    0.8635    0.8633    0.0000   -0.8633   -0.8635   -0.0000    0.8658    0.8612    0.0091   -0.8821   -0.8241];
%39 tap
input=[0.1969    0.8309    0.8815   -0.0099   -0.8613   -0.8698    0.0031    0.8655    0.8670    0.0000   -0.8670   -0.8655   -0.0031    0.8698    0.8613    0.0099   -0.8815   -0.8309];

t = 1:1:2*length(input); % time
t_alt = t(1:2:end);

% upsample
upsampledInput = zeros(1,length(t));
upsampledInput(1:2:end) = input;

% hbFilter
% hbFilter = [-0.0016    0.0000    0.2330    0.5000    0.2330    0.0000   -0.0016];

% hbFilter = [-0.0085    0.0000    0.2451    0.5000    0.2451    0.0000   -0.0085];
% hbFilter= [-0.0023    0.0000    0.0054   -0.0000   -0.0159    0.0000    0.0385   -0.0000   -0.0893    0.0000    0.3124    0.5000    0.3124    0.0000   -0.0893   -0.0000   0.0385    0.0000   -0.0159   -0.0000    0.0054    0.0000   -0.0023];
hbFilter = [-0.0013    0.0000    0.0020   -0.0000   -0.0038    0.0000    0.0071   -0.0000   -0.0124    0.0000    0.0204   -0.0000   -0.0330    0.0000    0.0542   -0.0000   -0.1002    0.0000    0.3163    0.5000    0.3163    0.0000   -0.1002   -0.0000    0.0542    0.0000   -0.0330   -0.0000    0.0204    0.0000   -0.0124   -0.0000   0.0071    0.0000   -0.0038   -0.0000    0.0020    0.0000   -0.0013];

% hbFilter convolution
y_conv = conv(hbFilter,upsampledInput);

% remove extra samples
l = (length(hbFilter)-1)/2;
interpolatedOutput = y_conv(l+1:l+length(upsampledInput));

%% plotting figures

figure
subplot(3,1,1);
stem(t_alt,input,"filled",'o'); 
title('Input Signal');

subplot(3,1,2);
stem(t,upsampledInput,"filled",':s','Color', 'r');
title('upsampled Input signal');

subplot(3,1,3);
stem(t,interpolatedOutput,"filled",'--','Color', 'g');
title('Interpolated output signal');
grid on;


Fs = 1200;                      % samples per second
dt = 1/Fs;                     % seconds per sample
StopTime = 0.03;                  % seconds
t1 = (0:dt:StopTime-dt)';
N = size(t1,1);
X = fftshift(fft(interpolatedOutput));
dF = Fs/N;                      % hertz
f = -Fs/2:dF:Fs/2-dF;           % hertz
figure;
subplot(2,1,1);
plot(t1,interpolatedOutput);
title('Interpolated output signal');
subplot(2,1,2);
plot(f,abs(X)/N);
xlabel('Frequency (in hertz)');
title('Magnitude Response');

X_up = fftshift(fft(upsampledInput));
figure;
subplot(2,1,1);
plot(t1,upsampledInput);
title('upsampled output signal');
subplot(2,1,2);
plot(f,abs(X_up)/N);
xlabel('Frequency (in hertz)');
title('Magnitude Response');