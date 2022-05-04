function [ ...
    external_force, ...  % 经傅里叶展开后的外力函数
    displacement_nodump, ...  % 无阻尼时的位移函数
    displacement_dump ...  % 存在阻尼时的位移函数
    ] = method_fourier_unfolds( ...
                               t1, ...  % 前半周期时长
                               t2, ...  % 后半周期时长
                               exact_external_force_1, ...
                               exact_external_force_2, ...
                               expand_num, ...  % 傅里叶展开项数
                               omega, ...  % 体系固有频率
                               k, ...  % 结构刚度系数
                               kesai ...  % 阻尼比
                               )
T = t1 + t2;  % 荷载总周期
theta=2*pi/T;  % 外荷载频率

% 分段函数进行傅里叶展开的核心代码
syms t n;
a0=1/T * integrals('t',exact_external_force_1,0,t1,exact_external_force_2,t1,T);
an=2/T * integrals('t',exact_external_force_1*cos(n*theta*t),0,t1,exact_external_force_2*cos(n*theta*t),t1,T);
bn=2/T * integrals('t',exact_external_force_1*sin(n*theta*t),0,t1,exact_external_force_2*sin(n*theta*t),t1,T);

% 初始化必要的值
displacement_nodump = 0;
displacement_dump = 0;
beta = 1:expand_num;
miu = 1:expand_num;
external_force = 0;

% 以传入的傅里叶展开项数进行计算，最后将结果叠加即是傅里叶展开的近似
for n=1:expand_num
    % 以下运算没有复杂的逻辑，也未涉及复杂的循环迭代，只需要按数学表达式写出即可
    beta(n) = n*theta/omega;
    miu(n) = abs(1./(1-beta(n).^2));
    epsilon = atan(2*kesai*beta(n)/(1-beta(n).^2));
    miu_dump = 1./((1-beta(n).^2).^2+(2*kesai*beta(n)).^2).^0.5;
    
    displacement_nodump=displacement_nodump + miu(n) .* vpa(eval(an*cos(n*theta.*t)+bn*sin(n*theta.*t)));
    if (nargin > 7 )  % 若输入值大于7，说明需要同时计算有阻尼和无阻尼情况，否则只计算无阻尼情况
        displacement_dump = displacement_dump + miu_dump .* vpa(eval(an*cos(n*theta.*t-epsilon)+bn*sin(n*theta.*t-epsilon)));
    end
    external_force = external_force+vpa(eval(an)*cos(n*theta.*t)+eval(bn)*sin(n*theta.*t));
end

external_force = external_force+a0;  % 返回作用力P的表达式
displacement_nodump = (displacement_nodump+double(a0))/k;  % 返回无阻尼时的位移表达式
displacement_dump = (displacement_dump+double(a0))/k;  % 返回有阻尼时的位移表达式
end
