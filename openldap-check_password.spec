%define upstream_name check_password

Name:       openldap-%{upstream_name}
Version:    1.0.3
Release:    2
Summary:    OpenLdap password checker module
License:    Artistic
Group: 		System/Servers
URL: 		http://linagora.org/contrib/annuaires/extensions/openldap_ppolicy_check_password
Source0: 	http://tools.ltb-project.org/attachments/download/29/%{upstream_name}-%{version}.tar.gz
BuildRequires: openldap-devel
BuildRequires: cracklib-devel
BuildRequires: libwrap-devel
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
check_password.c is an OpenLDAP pwdPolicyChecker module used to check the
strength and quality of user-provided passwords.

This module is used as an extension of the OpenLDAP password policy controls,
see slapo-ppolicy(5) section pwdCheckModule.

check_password.c will run a number of checks on the passwords to ensure minimum
strength and quality requirements are met. Passwords that do not meet these
requirements are rejected. 

%prep
%setup -q -n %{upstream_name}-%{version}

%build
%make \
    LDAP_INC="-I%{_includedir}/openldap/include -I%{_includedir}/openldap/slapd"


%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}/%{_libdir}/openldap
install -m 755 check_password.so %{buildroot}/%{_libdir}/openldap

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README INSTALL LICENSE
%{_libdir}/openldap/*



%changelog
* Fri Jul 17 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.3-1mdv2010.0
+ Revision: 396867
- new version, new URL
- hard code libwrap-devel for backports (openldap package has been fixed in 2009.0 only)

* Mon Sep 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.2-1mdv2009.0
+ Revision: 284946
- import openldap-check_password


* Mon Sep 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.2-1mdv2009.0
- first mdv release
