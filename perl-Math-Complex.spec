%define upstream_name    Math-Complex
%define upstream_version 1.59

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 1.59
Release:	3

Summary:	Complex numbers and associated mathematical functions
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Math/Math-Complex-1.59.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
'Math::Trig' defines many trigonometric functions not defined by the core
Perl which defines only the 'sin()' and 'cos()'. The constant *pi* is also
defined as are a few convenience functions for angle conversions, and
_great circle formulas_ for spherical movement.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc ChangeLog
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Wed Jun 22 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.580.0-1mdv2011.0
+ Revision: 686640
- update to new version 1.58

* Mon May 09 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.570.0-1
+ Revision: 672854
- update to new version 1.57

* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 1.560.0-2
+ Revision: 654250
- rebuild for updated spec-helper

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 1.560.0-1mdv2011.0
+ Revision: 401634
- rebuild using %%perl_convert_version
- fixed license field

* Mon May 11 2009 Jérôme Quelin <jquelin@mandriva.org> 1.56-1mdv2010.0
+ Revision: 374531
- import perl-Math-Complex


* Mon May 11 2009 cpan2dist 1.56-1mdv
- initial mdv release, generated with cpan2dist


