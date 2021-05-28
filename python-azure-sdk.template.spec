# Enable Python dependency generation
%{?python_enable_dependency_generator}


Name:           python-azure
Version:        20210527
Release:        1%{?dist}

Summary:        Azure SDK for Python
License:        MIT
URL:            https://github.com/Azure/azure-sdk-for-python
{% for package in packages -%}
{% set source_label = "Source" + ((loop.index - 1) | string) + ":" -%}
{{ source_label.ljust(16) }}%{pypi_source {{ package.name }} {{ package.version }} {{ package.extension }}}
{% endfor %}

BuildArch:      noarch

Obsoletes:      python-azure-sdk == 5.0.0-4

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Azure SDK for Python

{% for package in packages %}
%package {{ package.short_name }}
Version: {{ package.version}}
Summary: {{ package.summary}}

%description {{ package.short_name }}
{{ package.summary}}
{% endfor %}

%prep
# Create the base directory but skip any extractions for now.
%autosetup -n %{name}-%{version} -c -T
{% for package in packages -%}
# Extract {{ package.name }} {{ package.version }}
%autosetup -n %{name}-%{version} -D -T -a {{ loop.index - 1 }}
{% endfor %}

%build
PYTHON_PROJECTS=$(find . -name setup.py -maxdepth 2)
for PYTHON_PROJECT in $PYTHON_PROJECTS; do
    pushd $(dirname $PYTHON_PROJECT)
        %py3_build
    popd
done

%install
PYTHON_PROJECTS=$(find . -name setup.py -maxdepth 2)
for PYTHON_PROJECT in $PYTHON_PROJECTS; do
    pushd $(dirname $PYTHON_PROJECT)
        %py3_install
    popd
done

rm -rf %{buildroot}%{python3_sitelib}/{doc,samples,tests}

%files
%{python3_sitelib}/azure/__init__.py
%{python3_sitelib}/azure/__pycache__/__init__*


{% for package in packages %}
%files {{ package.short_name }}
{% for file_type, file_path in package.files.items() -%}
{{ file_path }}
{% endfor %}
{% endfor %}

%changelog
* Thu May 27 2021 Major Hayden - 20210527-1
- First package.
