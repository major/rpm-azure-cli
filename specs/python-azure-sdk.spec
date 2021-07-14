# Commit corresponding to the 5.0.0 release of the azure bundle on PyPi
%global commit 2b2cfd46758e7b9d55346f79f05592d7488c1bd0
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global srcname azure-sdk
%global _description %{expand:This project provides a set of Python packages that make it easy to access
Management (Virtual Machines, ...) or Runtime (ServiceBus using HTTP, Batch,
Monitor) components of Microsoft Azure Complete feature list of this repo and
where to find Python packages not in this repo can be found on our Azure SDK for
Python documentation.}

# Too many tests require an Internet connection
%global _with_tests 1
%global _with_doc 1

Name:           python-%{srcname}
Version:        5.0.0
Release:        9%{?dist}
Summary:        Microsoft Azure SDK for Python

# All packages are licensed under the MIT license, except
# azure-servicemanagement-legacy
License:        MIT and ASL 2.0
URL:            https://github.com/Azure/azure-sdk-for-python
Source0:        %{url}/archive/%{shortcommit}/%{srcname}-%{shortcommit}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
BuildArch:      noarch

%description
%{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
%py_provides python3-%{srcname}
Provides:       python3-azure-storage = %{version}-%{release}
Obsoletes:      python3-azure-storage < 2.1.0-4

%description -n python3-%{srcname}
%{_description}


%prep
%autosetup -p0 -n %{srcname}-for-python-%{commit}


%build


%install


%files -n python3-%{srcname}




%changelog
* Wed Jul 14 2021 Major Hayden <major@mhtx.net> - 5.0.0-9
- Empty package.

* Tue Jul 13 2021 Major Hayden <major@mhtx.net> - 5.0.0-8
- Remove azure-devtools provides.

* Tue Jul 06 2021 Major Hayden <major@mhtx.net> - 5.0.0-7
- Revert the previous commit that removed items from this package for obsoletion.

* Tue Jul 06 2021 Major Hayden <major@mhtx.net> - 5.0.0-6
- Prepare package for obsoletion.

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 5.0.0-5
- Rebuilt for Python 3.10

* Sun Feb 14 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 5.0.0-4
- Fix documentation build with new RTD theme (RHBZ #1913781)
- Re-enable tests

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 5.0.0-2
- Rebuilt

* Wed Jul 01 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 5.0.0-1
- Update to 5.0.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.0.0-12
- Bootstrap for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.0-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Wed Aug 28 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 4.0.0-9
- Re-enable tests

* Wed Aug 28 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 4.0.0-8
- Disable tests to rebuild package without python-azure-storage (for Python 3.8
  rebuild)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.0-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 4.0.0-5
- Enable Python generators
- Enable tests
- Spec cleanup

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 22 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 4.0.0-3
- Build documentation with Python 3 on Fedora
- Fix Python 3-only file deployment
- Don't glob everything under the Python sitelib directory

* Mon Aug 06 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 4.0.0-2
- Delete all Python 3-only files from the python2 subpackage

* Mon Aug 06 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 4.0.0-1
- Update to 4.0.0
