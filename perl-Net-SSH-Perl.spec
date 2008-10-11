%define	module	Net-SSH-Perl
%define	name	perl-%{module}
%define	version	1.31
%define	release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Perl client Interface to SSH
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(MIME::Base64)
BuildRequires:	perl(Math::Pari)
BuildRequires:	perl(Math::GMP)
BuildRequires:  perl(String::CRC32)
BuildRequires:  perl(Convert::PEM)
BuildRequires:  perl(Crypt::IDEA)
BuildRequires:  perl(Crypt::DH)
BuildRequires:  perl(Crypt::DSA)
BuildRequires:  perl(Digest::SHA1)
BuildRequires:  perl(Digest::HMAC)
BuildRequires:	perl(Digest::MD5)
BuildRequires:  perl(Digest::BubbleBabble)
BuildRequires:  perl(Crypt::RSA)
BuildArch:      noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Net::SSH::Perl is an all-Perl module implementing an SSH
(Secure Shell) client. It is compatible with both the SSH-1
and SSH-2 protocols.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor < /dev/null
%make

%check
# test hang... :\
# %{__make} test

%install
rm -rf %{buildroot}
%{makeinstall_std}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Net
%{_mandir}/man*/*

