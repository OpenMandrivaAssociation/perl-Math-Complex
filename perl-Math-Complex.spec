
%define realname   Math-Complex
%define version    1.56
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Tan asin acos sinh cosh tanh sech cosech
Source:     http://www.cpan.org/modules/by-module/Math/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More)

BuildArch: noarch

%description
'Math::Trig' defines many trigonometric functions not defined by the core
Perl which defines only the 'sin()' and 'cos()'. The constant *pi* is also
defined as are a few convenience functions for angle conversions, and
_great circle formulas_ for spherical movement.





%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc ChangeLog
%{_mandir}/man3/*
%perl_vendorlib/*


