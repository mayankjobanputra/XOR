import math
#Sigmoid function
def sigmoid(x):
    return 1/(1 + math.exp(-x));
#
in1 = 0;in2 = 0; Target = 1;
#
Wy = 1;Womg = 1;
Walpy = 1;Walpomg = 1;
Wbetay = 1;Wbetaomg = 1;
WAalp = 1;WAbeta=1;
#Feed Forward part
#in_y = in1*Wy; in_omg = in2*Womg;
O_y = sigmoid(in1*Wy); O_omg = sigmoid(in2*Womg);
#
#in_alpy = O_y*Walpy; in_betay = O_y*Wbetay; 
#in_alpomg = O_omg*Walpomg; in_betaomg = O_omg*Wbetaomg ;
# 
O_alp = sigmoid((O_y*Walpy+O_omg*Walpomg)); O_beta = sigmoid(O_y*Wbetay+O_omg*Wbetaomg);
#in_Aalp = O_alp*WAalp ;in_Abeta = O_beta * WAbeta;
#
O_A = sigmoid((O_alp*WAalp+O_beta * WAbeta));
#
#Error calculation and backpropagation part
E_A = math.pow((Target - O_A),2)/2;
#change in weight edge of A, alpha and A, Beta
dW_Aalp = E_A*O_A*WAalp; 
dW_Abeta = E_A*O_A*WAbeta;
#Error calculation for alpha , beta , y ,omg
E_alp = E_A*WAalp;
E_beta = E_A*WAbeta;
E_y = O_y*(1-O_y)*((E_alp*Walpy)+(E_beta*Wbetay));
E_omg = O_omg*(1-O_omg)*((E_alp*Walpomg)+(E_beta*Wbetaomg));
#change in weight edge of alpha, y and Beta, Y and alpha, omg and Beta, omg
dW_alpy = E_alp*O_alp*(1-O_alp)*Walpy; 
dW_alpomg = E_alp*O_alp*(1-O_alp)*Walpomg;
dW_betay = E_beta*O_beta*(1-O_beta)*Wbetay; 
dW_betaomg = E_beta*O_beta*(1-O_beta)*Wbetaomg;
dW_y = E_y*Wy;
dW_omg = E_omg*Womg; 
#
print E_A;
print "Welcome to XOR";
print "first layer neurons are y and Omg,\nsecond layer neurons are alpha and beta and A is output\nW denotes weights";
#
while E_A!=0.0000000000:
    
    in1 = int(raw_input("Enter input 1"));
    in2 = int(raw_input("Enter input 2"));
    Target = int(raw_input("Enter Target"));
    #
    Wy = Wy + dW_y;
    Womg = Womg +dW_omg;
    Walpy = Walpy + dW_alpy;
    Walpomg = Walpomg + dW_alpomg;
    Wbetay = Wbetay + dW_betay;
    Wbetaomg = Wbetaomg + dW_betaomg;
    WAalp = WAalp + dW_Aalp;
    WAbeta= WAbeta + dW_Abeta;
    #
    #Feed Forward part
    #
    O_y = sigmoid(in1*Wy); O_omg = sigmoid(in2*Womg);
    #
    O_alp = sigmoid((O_y*Walpy+O_omg*Walpomg)); O_beta = sigmoid(O_y*Wbetay+O_omg*Wbetaomg);
    #
    O_A = sigmoid((O_alp*WAalp+O_beta * WAbeta));
    #
    #Error calculation and backpropagation part
    E_A = math.pow((Target - O_A),2)/2;
    print E_A;
    #change in weight edge of A, alpha and A, Beta
    dW_Aalp = E_A*O_A*WAalp; 
    dW_Abeta = E_A*O_A*WAbeta;
    #
    #Error calculation for alpha , beta , y ,omg
    E_alp = E_A*WAalp;
    E_beta = E_A*WAbeta;
    E_y = O_y*(1-O_y)*((E_alp*Walpy)+(E_beta*Wbetay));
    E_omg = O_omg*(1-O_omg)*((E_alp*Walpomg)+(E_beta*Wbetaomg));
    #
    #change in weight edge of alpha, y and Beta, Y and alpha, omg and Beta, omg
    dW_alpy = E_alp*O_alp*(1-O_alp)*Walpy; 
    dW_alpomg = E_alp*O_alp*(1-O_alp)*Walpomg;
    dW_betay = E_beta*O_beta*(1-O_beta)*Wbetay; 
    dW_betaomg = E_beta*O_beta*(1-O_beta)*Wbetaomg;
    dW_y = E_y*Wy;
    dW_omg = E_omg*Womg; 
    
    
print "Work Done";  
