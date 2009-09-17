#include <map>
#include <vector>
#include <list>
#include <deque>
#include <bitset>
#include <set>
#include <string>


namespace {
  struct dictionary {
  std::bitset<7> dummybitset7;
  std::vector<unsigned long> dummy1;
  std::vector<unsigned int> dummy2;
  std::vector<std::vector<unsigned int> > dummy2v;
  std::vector<long> dummy3;
  std::vector<int> dummy4;
  std::vector<std::vector<int> > dummy4v;
  std::vector<std::string> dummy5;
  std::vector<char> dummy6;
  std::vector<char*> dummy6p;
  std::vector<unsigned char> dummy7;
  std::vector<unsigned char*> dummy7p;
  std::vector<short> dummy8;
  std::vector<unsigned short> dummy9;
  std::vector<std::vector<unsigned short> > dummy9v;
  std::vector<double> dummy10;
  std::vector<std::vector<double> > v_v_d;  
  std::vector<long double> dummy11;
  std::vector<float> dummy12;
  std::vector<bool> dummy13;
  std::vector<unsigned long long> dummy14;
  std::vector<long long> dummy15;
  std::vector<std::pair<std::basic_string<char>,double> > dummy16;
  std::vector<std::pair<unsigned int,double> > dummy16_1;
  std::vector<std::pair<int,int> > dummy16_2;
  std::vector<std::pair<double,double> > dummy16_3;
  std::vector<std::pair<float,float> > dummy16_4;
  std::vector<std::map<short,short> > dummy16_5;
  std::vector<std::vector<std::vector<int> > > dummy16_6;
  std::list<int> dummy17;
  std::deque<int> dummy18;
  std::set<int> dummy19;
  std::set<std::basic_string<char> > dummy20;
  std::pair<unsigned long, unsigned long> dummywp1;
  std::pair<unsigned int, unsigned int> dummywp2;
  std::pair<unsigned int, int> dummywp2_1;
  std::pair<unsigned int, unsigned long> dummywp2_2;
  std::pair<unsigned short, unsigned short> dummywp3;
  std::pair<int, int> dummywp4;
  std::pair<unsigned int, bool> dummywp5;
  std::pair<unsigned int, float> dummywp6;
  std::pair<const unsigned int, float> dummywp6a;
  std::pair<unsigned int, double> dummywp6d;
  std::pair<double, double> dummywp7;
  std::pair<double, std::vector<double> > dummywp7v;
  std::pair<float,float> dummywp7ff;
  std::pair<unsigned long long, std::basic_string<char> > dummywp8;
  std::pair<std::basic_string<char>,int> dummywp9;
  std::pair<std::basic_string<char>,double> dummywp10;
  std::pair<std::basic_string<char>,float> dummywp101;
  std::pair<std::basic_string<char>,bool> dummywp102;
  std::pair<std::basic_string<char>,std::vector<std::pair<std::basic_string<char>,double> > > dummywp11;
  std::pair<std::basic_string<char>,std::vector<std::basic_string<char> > > dummywp12;
  std::pair<unsigned int,std::vector<unsigned int> > dummywp13;
  std::pair<unsigned long,std::vector<unsigned long> > dummywp14;
  std::pair<unsigned short,std::vector<unsigned short> > dummywp15;
  std::pair<int,std::pair<unsigned int,unsigned int> > dummywp16;
  std::pair<int,std::pair<unsigned long,unsigned long> > dummywp17;
  std::pair<unsigned int,short> dummywp18;
  std::pair<unsigned int,std::vector<std::pair<unsigned int,double> > > dummywp19;
  std::pair<int,double> p_i_d;
  std::pair<const unsigned int,std::basic_string<char> > dummypcis;
  std::pair<short,short> dummyss;
  std::pair<short,std::vector<short> > dummysvs;
  std::pair<std::basic_string<char>,std::basic_string<char> > dummystst;
  std::pair<std::basic_string<char>,std::map<std::basic_string<char>,std::basic_string<char> > > dummysmss;
  std::pair<std::pair<short,short>,std::pair<short,std::vector<short> > > dummypsspsvs;
  std::vector<std::pair<int,double> > v_p_i_d;
  std::vector<std::vector<std::pair<int,double> > > v_v_p_i_d;


  std::vector<std::pair<std::basic_string<char>, float> >	 v_p_s_f;
  std::vector<std::pair<std::basic_string<char>, int> >	 v_p_s_i32;
  std::vector<std::pair<std::basic_string<char>, bool> > v_p_s_b;
  std::vector<std::pair<unsigned long long,std::basic_string<char> > > v_ull_s;

  std::map<unsigned long, unsigned long> dummywm1;
  std::map<unsigned int, unsigned int> dummywm2;
  std::pair<const unsigned int, unsigned int> dummywm2_valuetype;
  std::map<unsigned int, int> dummywm2_1;
  std::map<unsigned short, unsigned short> dummywm3;
  std::map<int, int> dummywm4;
  std::map<unsigned int, bool> dummywm5;
  std::map<unsigned int, short> dummywm6;
  std::pair<const unsigned int, short> dummywm6_valuetype;

  std::map<unsigned long, std::vector<unsigned long> > dummywmv1;
  std::map<unsigned int, std::vector<unsigned int> > dummywmv2;
  std::map<unsigned int,std::vector<std::pair<unsigned int,double> > >dummywmv2_1;
  std::map<unsigned short, std::vector<unsigned short> > dummypwmv3;
  std::map<unsigned int, float> dummywmuif;
  std::map<unsigned int, double> dummywmuid;
  std::map<unsigned long long, std::basic_string<char> > dummyypwmv5;
  std::multimap<double, double> dummyypwmv6;
  std::map<std::basic_string<char>,int> dummyypwmv7;
  std::map<std::string, std::string> dummymss1;
  std::pair<const std::string, std::string> dummymss1_valuetype;
  std::map<std::basic_string<char>,std::vector<std::pair<std::basic_string<char>,double> > > dummyypwmv8;
  std::map<int,std::pair<unsigned int,unsigned int> > dummyypwmv9;
  std::map<int,std::pair<unsigned long,unsigned long> > dummyypwmv10;
  std::map<std::basic_string<char>,std::vector<std::basic_string<char> > > dummyypwmv11;
  std::map<short,short> dummymss;
  std::map<std::basic_string<char>,std::map<std::basic_string<char>,std::basic_string<char> > > dummymsmss;
  std::map<std::basic_string<char>,std::pair<unsigned int,unsigned int> > dummymspii;
  std::map<std::pair<short,short>,std::pair<short,std::vector<short> > > dummympsspsvs;
  std::map<unsigned int,std::basic_string<char> > dummymuis;
  std::map<unsigned int,std::pair<unsigned int,unsigned int> > dummymuipuu;
  std::vector<char>::iterator itc;
  std::vector<short>::iterator its;
  std::vector<unsigned short>::iterator itus;
  std::vector<int>::iterator iti;
  std::vector<unsigned int>::iterator itui;
  std::vector<long>::iterator itl;
  std::vector<unsigned long>::iterator itul;
  std::vector<long long>::iterator itll;
  std::vector<unsigned long long>::iterator itull;
  std::vector<float>::iterator itf;
  std::vector<double>::iterator itd;
  std::vector<long double>::iterator itld;
  std::vector<std::string>::iterator itstring;
  std::vector<void *>::iterator itvp;
  std::allocator<char> achar;
  std::allocator<short> ashort;
  std::allocator<int> aint;
  std::allocator<double> adouble;
};
}
