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
Summary(es):	M�dulo de Perl Net::IP
Summary(fr):	Module Perl Net::IP
Summary(it):	Modulo di Perl Net::IP
Summary(ja):	Net::IP Perl �⥸�塼��
Summary(ko):	Net::IP �� ����
Summary(no):	Perlmodul Net::IP
Summary(pl):	Modu� perla Net::IP
Summary(pt_BR):	M�dulo Perl Net::IP
Summary(pt):	M�dulo de Perl Net::IP
Summary(ru):	������ ��� Perl Net::IP
Summary(sv):	Net::IP Perlmodul
Summary(uk):	������ ��� Perl Net::IP
Summary(zh_CN):	Net::IP Perl ģ��
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
Net::IP - wsparcie dla protoko�u IP.

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
