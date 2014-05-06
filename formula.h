#include <string>
#include <iostream>

class Formula {
  public:
    Formula* phi_ptr;
    Formula* psi_ptr;
    virtual void print() {};
};

class Variable : public Formula {
  public:
    Variable(std::string _p) : p(_p) {}
    std::string p;
    void print() {std::cout << p << " ";}
};

class Conjunction : public Formula {
  public:
    Conjunction(Formula _p, Formula _q) : phi(_p), psi(_q) {phi_ptr = &phi;
                                                            psi_ptr = &psi;}
    Formula phi;
    Formula psi;
    void print() {std::cout << "("; 
                  phi.print(); 
                  std::cout << "^";
                  psi.print();
                  std::cout << ") ";}
};

class Disjunction : public Formula {
  public:
    Disjunction(Formula _p, Formula _q) : phi(_p), psi(_q) {phi_ptr = &phi;
                                                            psi_ptr = &psi;}
    Formula phi;
    Formula psi;
    void print() {std::cout << "("; 
                  phi.print(); 
                  std::cout << "v";
                  psi.print();
                  std::cout << ") ";}
};

class Negation : public Formula {
  public:
    Negation(Formula _p) : phi(_p) {phi_ptr = &phi;}
    Formula phi;
    void print() {std::cout <<"~(";
                  phi.print(); 
                  std::cout << ") ";}
};
