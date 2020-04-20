from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path(
        "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
    ),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("users/", include("scieio.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
    path("products/", include("generals.categories.urls")),
    path("analytical-instruments/", include("instruments.analytical_instruments.urls")),
    path("chromatography/", include("instruments.chromatography.urls")),
    path("brands/", include("generals.manufacturers.urls")),
    path("sellers/", include("generals.sellers.urls")),
    path("product-conditions/", include("generals.conditions.urls")),
    path("mass-spectrometry/", include("instruments.spectrometry.urls")),
    path("spectroscopy/", include("instruments.spectroscopy.urls")),
    path("elemental-analyzers/", include("instruments.elemental_analyzers.urls")),
    path("life-sciences/", include("biology.life_sciences.urls")),
    path("dna-synthesizers/", include("biology.dna_synthesizers.urls")),
    path("microarray-scanners/", include("biology.microarray.urls")),
    path("immunoassay-systems/", include("biology.immunoassay.urls")),
    path("biotechnology/", include("biology.biotechnology.urls")),
    path("fermenters-and-bioreactors/", include("biology.bioreactors.urls")),
    path("dna-sequencers/", include("biology.dna_sequencer.urls")),
    path("bonders/", include("testers.bonders.urls")),
    path("disposition/", include("testers.disposition.urls")),
    path("viscometer-and-rheometer/", include("testers.viscometers.urls")),
    path("test-and-semiconductor/", include("testers.tests_semiconductors.urls")),
    path("hardness-tester/", include("testers.hardness.urls")),
    path("process-equipment/", include("process.process.urls")),
    path("food-processing-equipment/", include("process.food_processing.urls")),
    path("pharmaceutical-equipment/", include("process.pharmaceutical.urls")),
    path("water-treatment-equipment/", include("process.water_treatment.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
