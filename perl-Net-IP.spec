#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	IP
Summary:	Net::IP Perl module
Summary(cs):	Modul Net::IP pro Perl
Summary(da):	Perlmodul Net::IP
Summary(de):	Net::IP Perl Modul
Summary(es):	Módulo de Perl Net::IP
Summary(fr):	Module Perl Net::IP
Summary(it):	Modulo di Perl Net::IP
Summary(ja):	Net::IP Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Net::IP ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Net::IP
Summary(pl):	Modu³ perla Net::IP
Summary(pt_BR):	Módulo Perl Net::IP
Summary(pt):	Módulo de Perl Net::IP
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Net::IP
Summary(sv):	Net::IP Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Net::IP
Summary(zh_CN):	Net::IP Perl Ä£¿é
Name:		perl-Net-IP
Version:	1.13
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::IP Perl extension for the IP protocol.

%description -l pl
Net::IP - wsparcie dla protoko³u IP.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
perl Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
	
install ipcount $RPM_BUILD_ROOT%{_bindir}
install iptab $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Net/IP.pm
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man3/*
