clear all

%% 设置参数
m = 2e4;  % 小球质量
EI = 1e6;  % 刚度
L = 5;  % 杆长
k = 3*EI/(L^3);  % 计算体系刚度系数
w = (k/m)^0.5;  % 计算体系固有频率
p_max = 1000;  % 最大外力值

t1 = 1;  % 前半周期
t2 = 1;  % 后半周期

% 定义符合变量t
syms t
% 方波荷载
force_1 = 0*t+p_max;
force_2 = 0*t;

[external_force, displacement_nodump, displacement_dump] = ...
    method_fourier_unfolds(t1, t2, force_1, force_2, 50, w, k, 0.6);

len = 200;
y1 = 1:len;
y2 = 1:len;
p = 1:len;
time = 1:len;
t = 0;
for i=1:len
    t = t + 0.05;
    time(i) = t;
    y1(i) = eval(displacement_nodump);
    y2(i) = eval(displacement_dump);
    p(i) = eval(external_force);
end

subplot(2, 2, 1);
plot(time, y1);
title('无阻尼时位移与时间曲线');

subplot(2, 2, 2);
plot(time, y2);
title('有阻尼时位移与时间曲线');

subplot(2, 2, [3,4]);
plot(time, p);
title('傅里叶展开的外力函数图像');
