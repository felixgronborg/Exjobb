%% Load images -------------------------------------------------------
close all;
clear;
clc;

ej_slagskugga = double(imread('samling_ex_jobb/ej slagskugga.jpg')/255);
ljus_fonster_016 = double(imread('samling_ex_jobb/ljus_fonster_016.jpg')/255);
ljusa_lampor_010 = double(imread('samling_ex_jobb/ljusa_lampor_010.jpg')/255);
ljust_fonster_025 = double(imread('samling_ex_jobb/ljust_fonster_025.jpg')/255);
overexp_lampor = double(imread('samling_ex_jobb/overexp_lampor.jpg')/255);
overexponerat = double(imread('samling_ex_jobb/overexponerat.jpg')/255);
overexpred_color_cast = double(imread('samling_ex_jobb/red_color_cast.jpg')/255);
rorelseoskarpa_010 = double(imread('samling_ex_jobb/rorelseoskarpa_010.jpg')/255);
skev_bild_006 = double(imread('samling_ex_jobb/skev_bild_006.jpg')/255);
slagskugga_ = double(imread('samling_ex_jobb/slagskugga_.jpg')/255);
slagskugga_1 = double(imread('samling_ex_jobb/slagskugga_1.jpg')/255);
slagskuggor = double(imread('samling_ex_jobb/slagskuggor.jpg')/255);
% sned_bild_001 = double(imread('samling_ex_jobb/sned_bild_001.jpg')/255);
% sned_bild_004 = double(imread('samling_ex_jobb/sned_bild_004.jpg')/255);
% sned_bild_011 = double(imread('samling_ex_jobb/sned_bild_011.jpg')/255);
sned_exterior_039 = double(imread('samling_ex_jobb/sned_exterior_039.jpg')/255);
sned_exterior_044 = double(imread('samling_ex_jobb/sned_exterior_044.jpg')/255);
sned_fasad_040 = double(imread('samling_ex_jobb/sned_fasad_040.jpg')/255);
sned_for_mycket_himmel_045 = double(imread('samling_ex_jobb/sned_for_mycket_himmel_045.jpg')/255);

% color_fel_kall_028_g = rgb2gray(double(imread('samling_ex_jobb/color_fel_kall_028.jpg')/255));
% correct_colors_g = rgb2gray(double(imread('samling_ex_jobb/correct_colors.jpg')/255));
% ej_slagskugga_g = rgb2gray(double(imread('samling_ex_jobb/ej slagskugga.jpg')/255));
% green_fargstick_tak_g = rgb2gray(double(imread('samling_ex_jobb/green_fargstick_tak.jpg')/255));
% %gulstick_g = rgb2gray(double(imread('samling_ex_jobb/gulstick.jpg')/255));
% %gulstick_morkt_g = rgb2gray(double(imread('samling_ex_jobb/gulstick_morkt.jpg')/255));
% rorelseoskarpa_010_g = rgb2gray(double(imread('samling_ex_jobb/rorelseoskarpa_101.jpg')/255));
% skev_bild_006_g = rgb2gray(double(imread('samling_ex_jobb/skev_bild_006.jpg')/255));
% slagskugga__g = rgb2gray(double(imread('samling_ex_jobb/slagskugga_.jpg')/255));
% slagskugga_1_g = rgb2gray(double(imread('samling_ex_jobb/slagskugga_1.jpg')/255));
% slagskuggor_g = rgb2gray(double(imread('samling_ex_jobb/slagskuggor.jpg')/255));
% sned_bild_001_g = rgb2gray(double(imread('samling_ex_jobb/sned_bild_001.jpg')/255));
% sned_bild_004_g = rgb2gray(double(imread('samling_ex_jobb/sned_bild_004.jpg')/255));
% sned_bild_011_g = rgb2gray(double(imread('samling_ex_jobb/sned_bild_011.jpg')/255));
% sned_exterior_039_g = rgb2gray(double(imread('samling_ex_jobb/sned_exterior_039.jpg')/255));
% sned_exterior_044_g = rgb2gray(double(imread('samling_ex_jobb/sned_exterior_044.jpg')/255));
% sned_fasad_040_g = rgb2gray(double(imread('samling_ex_jobb/sned_fasad_040.jpg')/255));
% sned_for_mycket_himmel_045_g = rgb2gray(double(imread('samling_ex_jobb/sned_for_mycket_himmel_045.jpg')/255));
% sned_gul027_g = rgb2gray(double(imread('samling_ex_jobb/sned_gul027.jpg')/255));
%% Average Colors ----------------------------------------------------
close all;
clear;
clc;

color_fel_kall_028 = double(imread('samling_ex_jobb/color_fel_kall_028.jpg')/255);
correct_colors = double(imread('samling_ex_jobb/correct_colors.jpg')/255);
sned_gul027 = double(imread('samling_ex_jobb/sned_gul027.jpg')/255);
green_fargstick_tak = double(imread('samling_ex_jobb/green_fargstick_tak.jpg')/255);
gulstick_ = double(imread('samling_ex_jobb/gulstick_.jpg')/255);
gulstick_morkt = double(imread('samling_ex_jobb/gulstick_morkt.jpg')/255);

dim = 3543*5315;

avg_c_r = sum(sum(double(correct_colors(:,:,1))))/dim;
avg_c_g = sum(sum(double(correct_colors(:,:,2))))/dim;
avg_c_b = sum(sum(double(correct_colors(:,:,3))))/dim;

avg_w_r = sum(sum(double(red_color_cast(:,:,1))))/dim;
avg_w_g = sum(sum(double(sned_gul027(:,:,2))))/dim;
avg_w_b = sum(sum(double(sned_gul027(:,:,3))))/dim;

avg_c_im = zeros(1000,1000,3);
avg_c_im(:,:,1) = avg_c_r;
avg_c_im(:,:,2) = avg_c_g;
avg_c_im(:,:,3) = avg_c_b;

avg_w_im = zeros(1000,1000,3);
avg_w_im(:,:,1) = avg_w_r;
avg_w_im(:,:,2) = avg_w_g;
avg_w_im(:,:,3) = avg_w_b;

figure;
imshow(avg_c_im)
figure;
imshow(avg_w_im)

%% Exponering -------------------------------------------
%%
close all;
clear;
clc;

ljus_fonster_016_g = rgb2gray(double(imread('samling_ex_jobb/ljus_fonster_016.jpg')/255));
ljusa_lampor_010_g = rgb2gray(double(imread('samling_ex_jobb/ljusa_lampor_010.jpg')/255));
ljust_fonster_025_g = rgb2gray(double(imread('samling_ex_jobb/ljust_fonster_025.jpg')/255));
overexp_lampor_g = rgb2gray(double(imread('samling_ex_jobb/overexp_lampor.jpg')/255));
overexponerat_g = rgb2gray(double(imread('samling_ex_jobb/overexponerat.jpg')/255));
overexpred_color_cast_g = rgb2gray(double(imread('samling_ex_jobb/red_color_cast.jpg')/255));
underexponerat_g = rgb2gray(double(imread('samling_ex_jobb/underexponerat.jpg')/255));
gulstick_morkt_g = rgb2gray(double(imread('samling_ex_jobb/gulstick_morkt.jpg')/255));
%% Feature extraction
close all;
clear;
clc;

sned_bild_001 = imresize(imread('samling_ex_jobb/sned_bild_001.jpg'), 0.25);
sned_bild_004 = imresize(imread('samling_ex_jobb/sned_bild_004.jpg'), 0.25);
sned_bild_011 = imresize(imread('samling_ex_jobb/sned_bild_011.jpg'), 0.25);

% A = sned_bild_001;
A = sned_bild_004;
% A = sned_bild_011;


sigma = 0.8;
alpha = 0.1;

t_speed = timeit(@() locallapfilt(A, sigma, alpha, 'NumIntensityLevels', 5)) 

B_speed = locallapfilt(A, sigma, alpha, 'NumIntensityLevels', 5);
figure
imshow(B_speed)
title(['Enhanced with 5 intensity levels in ' num2str(t_speed) ' sec'])


%% Convert to BW
close all;
% clear;
clc;
I = imresize(imread('samling_ex_jobb/sned_bild_011.jpg'), 0.2);
grayI = rgb2gray(I);
% figure;
% imshow(grayI)
neighbourhood = (2*floor(size(I)/128)+1)
I_histeq = histeq(grayI);
I_adapthisteq = adapthisteq(grayI);

T = adaptthresh(I_histeq);

I_BW = imbinarize(I_histeq, 'adaptive');
% figure;
% imshow(I_BW);
%% Hough transformation
close all;
clear;
clc;
I = rgb2gray(imresize(imread('samling_ex_jobb/sned_bild_001.jpg'), 0.7));
% I = im2bw(double(rgb2gray(imresize(imread('samling_ex_jobb/sned_bild_011.jpg'), 0.7))), 0.5);
I = imrotate(I,90);
rotI = imrotate(I,33);
BW = edge(rotI,'canny');

[H,T,R] = hough(BW);
imshow(H,[],'XData',T,'YData',R,...
            'InitialMagnification','fit');
xlabel('\theta'), ylabel('\rho');
axis on, axis normal, hold on;

P  = houghpeaks(H,5,'threshold',ceil(0.3*max(H(:))));
x = T(P(:,2)); y = R(P(:,1));
plot(x,y,'s','color','white');

lines = houghlines(BW,T,R,P,'FillGap',10,'MinLength',100);
figure, imshow(rotI), hold on
max_len = 0;
for k = 1:length(lines)
   xy = [lines(k).point1; lines(k).point2];
   plot(xy(:,1),xy(:,2),'LineWidth',2,'Color','green');

   % Plot beginnings and ends of lines
   plot(xy(1,1),xy(1,2),'x','LineWidth',2,'Color','yellow');
   plot(xy(2,1),xy(2,2),'x','LineWidth',2,'Color','red');

   % Determine the endpoints of the longest line segment
   len = norm(lines(k).point1 - lines(k).point2);
   if ( len > max_len)
      max_len = len;
      xy_long = xy;
   end
end

plot(xy_long(:,1),xy_long(:,2),'LineWidth',2,'Color','cyan');



