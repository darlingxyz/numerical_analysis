function  [ output ]  = integrals( ...  % 此处默认外力的分段函数为两段
                              t, ...  % 积分变量
                              fx_1, ...  % 第一段函数表达式
                              leftInterval_1, ...  % 左区间
                              rightInterval_1, ...  % 右区间
                              fx_2, ...  % 第二段函数表达式
                              leftInterval_2, ... % 左区间
                              rightInterval_2 ...  % 右区间
                              )
output=int(fx_1,t,leftInterval_1,rightInterval_1) +  ... % 计算第一段函数的积分
       int(fx_2,t,leftInterval_2, rightInterval_2);  % 计算第二段函数的积分
end
